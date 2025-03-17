import streamlit as st
import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

# Load environment variables from a .env file (e.g., API keys)
load_dotenv()

# Configure the Gemini API using the API key from the environment variables
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini generative model
model = genai.GenerativeModel("gemini-1.5-pro")

def greet_user():
    """
    Displays a greeting and introduction to the user.
    This function sets up the title and a brief description of the app's purpose.
    """
    st.title("TalentScout Hiring Assistant")
    st.write("Hello! I'm here to assist with your initial screening for tech roles. "
             "I'll gather some information, ask technical questions based on your expertise, and guide you through the process. "
             "If you wish to end the conversation at any time, simply type 'exit' or 'quit'.")

def ask_answer():
    """
    Prompts the user to provide answers to the technical questions.
    This function is called after the candidate information is collected.
    """
    st.write("**Please provide answers to the following questions based on your expertise**")

def check_exit(input_text):
    """
    Checks if the user has entered any exit keywords to end the conversation.
    
    Args:
        input_text (str): The text input provided by the user.
    
    If an exit keyword is detected, the conversation is terminated.
    """
    exit_keywords = ["exit", "quit", "end"]
    if any(keyword in input_text.lower() for keyword in exit_keywords):
        st.warning("Conversation ended. Thank you for your time!")
        st.stop()

def fallback_response():
    """
    Provides a fallback response when the system cannot understand the user's input.
    This function is called in case of errors or unclear input.
    """
    st.write("I'm sorry, I didn't quite understand that. Could you please rephrase your input or provide more details?")

def gather_information():
    """
    Collects candidate information using a Streamlit form.
    The form includes fields for name, email, phone, experience, desired position, location, and tech stack.
    The collected data is stored in the session state for later use.
    """
    with st.form("candidate_info_form"):
        # Form fields for candidate information
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_input("Tech Stack (e.g., Python, Django, etc.)")
        submit = st.form_submit_button("Submit")

        if submit:
            # Check if the user wants to exit
            check_exit(name)
            
            # Validate that all fields are filled
            if not all([name, email, phone, experience, position, location, tech_stack]):
                st.error("❌ All fields are mandatory. Please fill out every field.")
            else:
                # Store candidate information in the session state
                st.session_state["candidate_info"] = {
                    "Name": name, "Email": email, "Phone": phone,
                    "Experience": experience, "Position": position,
                    "Location": location, "Tech Stack": tech_stack
                }
                st.success("✅ Information collected successfully!")

def generate_questions(tech_stack):
    """
    Generates technical questions based on the candidate's tech stack using the Gemini model.
    
    Args:
        tech_stack (str): The technology stack provided by the candidate.
    
    Returns:
        list: A list of generated technical questions.
    
    If questions are already generated for the same tech stack, they are reused from the session state.
    """
    # Check if questions are already generated for the same tech stack
    if "questions" in st.session_state and st.session_state.get("tech_stack") == tech_stack:
        return st.session_state["questions"]

    # Prompt for generating technical questions
    prompt = (
        f"Generate 3 to 5 technical interview questions for a candidate skilled in {tech_stack}. "
        "The questions should focus on practical knowledge, real-world application, "
        "theoretical understanding, and coding concepts. Ensure each question is clear, concise, "
        "and written on a new line without numbering or bullet points."
    )
    try:
        # Generate questions using the Gemini model
        response = model.generate_content(prompt)
        questions = [
            q.strip().lstrip("0123456789.- ")
            for q in response.text.strip().split("\n")
            if q.strip()
        ]
        # Limit the number of questions to 5
        questions = questions[:5] if len(questions) > 5 else questions
        
        # Store questions and tech stack in the session state
        st.session_state["questions"] = questions
        st.session_state["tech_stack"] = tech_stack
        return questions
    except Exception:
        # Handle errors during question generation
        fallback_response()
        return []

def show_questions():
    """
    Displays the generated technical questions and collects the candidate's responses.
    The responses are stored and displayed back to the user upon submission.
    """
    if "candidate_info" in st.session_state:
        tech_stack = st.session_state["candidate_info"].get("Tech Stack")
        if tech_stack:
            # Generate or retrieve questions for the tech stack
            questions = generate_questions(tech_stack)
            
            if not questions:
                st.error("Failed to generate questions. Please try again later.")
                return

            # Collect responses for each question
            responses = {}
            for idx, question in enumerate(questions, 1):
                st.write(f"**Q{idx}. {question}**")
                responses[question] = st.text_area("Write your response here", key=f"q_{idx}")

            # Display the responses upon submission
            if st.button("Submit"):
                st.write("### Your Responses")
                for idx, (q, ans) in enumerate(responses.items(), 1):
                    st.write(f"**Q{idx}. {q}**")
                    st.write(ans if ans else "No response provided")
                end_conversation()

def end_conversation():
    """
    Ends the conversation and thanks the candidate for their time.
    This function is called after the candidate submits their responses.
    """
    st.write("**Thank you for your time! We'll get back to you soon with the next steps.**")

def main():
    """
    Main function to run the Streamlit app.
    This function orchestrates the flow of the application:
    1. Greets the user.
    2. Collects candidate information.
    3. Asks technical questions and collects responses.
    """
    greet_user()
    gather_information()
    if "candidate_info" in st.session_state:
        ask_answer()
        show_questions()

# Entry point of the script
if __name__ == "__main__":
    main()

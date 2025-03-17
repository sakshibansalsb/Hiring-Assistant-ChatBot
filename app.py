import streamlit as st
import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini Model
model = genai.GenerativeModel("gemini-1.5-pro")

# Greeting and Intro
def greet_user():
    st.title("TalentScout Hiring Assistant")
    st.write("Hello! I'm here to assist with your initial screening for tech roles. "
             "I'll gather some information, ask technical questions based on your expertise, and guide you through the process. "
             "If you wish to end the conversation at any time, simply type 'exit' or 'quit'.")

def ask_answer():
    st.write("**Please provide answer of the following question based on your expertise**")

# Conversation Exit Handling
def check_exit(input_text):
    exit_keywords = ["exit", "quit", "end"]
    if any(keyword in input_text.lower() for keyword in exit_keywords):
        st.warning("Conversation ended. Thank you for your time!")
        st.stop()

# Fallback Response
def fallback_response():
    st.write("I'm sorry, I didn't quite understand that. Could you please rephrase your input or provide more details?")

# Collect Candidate Information
def gather_information():
    with st.form("candidate_info_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_input("Tech Stack (e.g., Python, Django, etc.)")
        submit = st.form_submit_button("Submit")

        if submit:
            check_exit(name)  # Check for exit keywords
            if not all([name, email, phone, experience, position, location, tech_stack]):
                st.error("❌ All fields are mandatory. Please fill out every field.")
            else:
                st.session_state["candidate_info"] = {
                    "Name": name, "Email": email, "Phone": phone,
                    "Experience": experience, "Position": position,
                    "Location": location, "Tech Stack": tech_stack
                }
                st.success("✅ Information collected successfully!")

# Generate Technical Questions
def generate_questions(tech_stack):
    if "questions" in st.session_state and st.session_state.get("tech_stack") == tech_stack:
        return st.session_state["questions"]

    prompt = (
        f"Generate 3 to 5 technical interview questions for a candidate skilled in {tech_stack}. "
        "The questions should focus on practical knowledge, real-world application, "
        "theoretical understanding, and coding concepts. Ensure each question is clear, concise, "
        "and written on a new line without numbering or bullet points."
    )
    try:
        response = model.generate_content(prompt)
        questions = [
            q.strip().lstrip("0123456789.- ")
            for q in response.text.strip().split("\n")
            if q.strip()
        ]
        questions = questions[:5] if len(questions) > 5 else questions
        st.session_state["questions"] = questions
        st.session_state["tech_stack"] = tech_stack
        return questions
    except Exception:
        fallback_response()
        return []

# Display Questions
def show_questions():
    if "candidate_info" in st.session_state:
        tech_stack = st.session_state["candidate_info"].get("Tech Stack")
        if tech_stack:
            questions = generate_questions(tech_stack)
            
            if not questions:
                st.error("Failed to generate questions. Please try again later.")
                return

            responses = {}
            for idx, question in enumerate(questions, 1):
                st.write(f"**Q{idx}. {question}**")
                responses[question] = st.text_area("Write your response here", key=f"q_{idx}")

            if st.button("Submit"):
                st.write("### Your Responses")
                for idx, (q, ans) in enumerate(responses.items(), 1):
                    st.write(f"**Q{idx}. {q}**")
                    st.write(ans if ans else "No response provided")
                end_conversation()

def end_conversation():
    st.write("**Thank you for your time! We'll get back to you soon with the next steps.**")

def main():
    greet_user()
    gather_information()
    if "candidate_info" in st.session_state:
        ask_answer()
        show_questions()
        
if __name__ == "__main__":
    main()

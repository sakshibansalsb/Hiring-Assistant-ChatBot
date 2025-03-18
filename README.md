# TalentScout Hiring Assistant

## Table of Contents

- [Project Overview](#project-overview)
- [Reference Images](#reference-images)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Prompt Engineering](#prompt-engineering)
- [Data Handling](#data-handling)
- [Challenges & Solutions](#challenges--solutions)

## Project Overview

The **TalentScout Hiring Assistant** is an intelligent chatbot designed to assist recruiters in conducting initial screenings for tech roles. It leverages the **Gemini 1.5 Pro** language model to generate technical questions based on the candidate's declared tech stack and collects essential candidate information for further evaluation. The chatbot provides a seamless and interactive experience for candidates while streamlining the hiring process for recruiters.

### Reference images  
<div align="center">
  <img src="https://github.com/user-attachments/assets/932f8749-5c72-4a1e-a53d-7734b36b4ab1" alt="Form" width="300" height="450">
  <img src="https://github.com/user-attachments/assets/29edee10-d0a8-4fae-8421-81205c5e621f" alt="Form" width="500" height="450">
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/299faa5d-dd53-4700-ae15-9d476fa308f0" alt="Form" width="500" height="450">
  <img src="https://github.com/user-attachments/assets/8b8bd8c2-ea8a-4305-9f00-4afeabe751d8" alt="Form" width="500" height="450">
</div>

## Features

- **Candidate Information Collection**: Collects essential details such as name, email, phone number, years of experience, desired position, location, and tech stack.
- **Dynamic Question Generation**: Generates 3 to 5 technical questions tailored to the candidate's tech stack using the Gemini 1.5 Pro model.
- **User-Friendly Interface**: Built using Streamlit for a clean and intuitive user experience.
- **Conversation Exit Handling**: Allows candidates to exit the conversation at any time by typing keywords like "exit," "quit," or "end."
- **Fallback Mechanism**: Provides meaningful responses when the chatbot does not understand the input.
- **Session Management**: Maintains session state to store candidate information and generated questions.

## Setup Instructions

### Prerequisites

- Python 3.7 or later
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/sakshibansalsb/Hiring-Assistant-ChatBot.git
    cd talentscout-hiring-assistant
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory with the following content:

    ```env
    GEMINI_API_KEY=your_actual_gemini_api_key_here
    ```

5. **Run the Application**

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Start the Application**: Run the application using the command `streamlit run app.py`.
2. **Greeting and Introduction**: The chatbot will greet you and explain its purpose.
3. **Collect Candidate Information**: Fill out the form with your details, including name, email, phone number, years of experience, desired position, location, and tech stack.
4. **Generate Technical Questions**: Based on your tech stack, the chatbot will generate 3 to 5 technical questions.
5. **Answer Questions**: Provide your answers to the questions directly in the application.
6. **Submit Responses**: Once you submit your responses, the chatbot will display your answers and end the conversation.

## Technical Details

- **Programming Language**: Python
- **Libraries & Tools**:
  - Streamlit: For the frontend interface.
  - Google Generative AI (Gemini): For generating technical questions.
  - Python-dotenv: For managing environment variables.
- **Model Used**: Gemini 1.5 Pro
- **Deployment**: Locally deployed using Streamlit. (Optional: Deployed on a cloud platform like AWS or GCP for bonus points.)

## Prompt Engineering

- **Information Gathering Prompts**: Designed to collect essential candidate details (e.g., "Please provide your full name, email address, and phone number.").
- **Technical Question Generation Prompts**: Example: "Generate 3 to 5 technical interview questions for a candidate skilled in Python and Django. Focus on practical knowledge, real-world application, and coding concepts."
- **Fallback Mechanism**: If the chatbot doesn’t understand the input, it responds with: "I'm sorry, I didn't quite understand that. Could you please rephrase your input or provide more details?"

## Data Handling

- **Simulated Data**: All candidate information is stored temporarily in the session state and is not persisted after the session ends.
- **Data Privacy**: No sensitive data is stored permanently. The application complies with data privacy best practices.

## Challenges & Solutions

- **Challenge 1**: Generating relevant technical questions for diverse tech stacks.
  - **Solution**: Designed prompts to focus on practical and theoretical aspects of the specified technologies.
- **Challenge 2**: Maintaining conversation context.
  - **Solution**: Used Streamlit’s session state to store candidate information and generated questions.
- **Challenge 3**: Handling unexpected user inputs.
  - **Solution**: Implemented a fallback mechanism to guide users to rephrase their inputs.

---

**TalentScout Hiring Assistant** is a powerful tool for recruiters looking to streamline their hiring process and engage candidates effectively. By leveraging the capabilities of the Gemini 1.5 Pro model, it provides a dynamic and efficient way to conduct initial screenings for tech roles.

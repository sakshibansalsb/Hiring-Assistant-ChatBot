# TalentScout Hiring Assistant

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Applications](#applications)
- [Contributing](#contributing)

## Project Overview

The **TalentScout Hiring Assistant** is a Streamlit-based application designed to assist recruiters in conducting initial screenings for tech roles. The application leverages the **Gemini 1.5 Pro** language model to generate technical questions based on the candidate's expertise and collects candidate information for further evaluation. The tool is designed to streamline the hiring process by automating the initial screening phase, saving time for recruiters and providing a seamless experience for candidates.

## Features

- **Candidate Information Collection**: Collects essential details such as name, email, phone number, years of experience, desired position, location, and tech stack.
- **Dynamic Question Generation**: Generates 3 to 5 technical questions tailored to the candidate's tech stack using the Gemini 1.5 Pro model.
- **Conversation Exit Handling**: Allows candidates to exit the conversation at any time by typing keywords like "exit," "quit," or "end."
- **Responsive Feedback**: Provides immediate feedback on the candidate's responses and guides them through the process.
- **Session Management**: Maintains session state to store candidate information and generated questions for a seamless user experience.

## Setup Instructions

To set up and run the **TalentScout Hiring Assistant** locally, follow these instructions:

### Prerequisites

- Python 3.7 or later
- Pip (Python package installer)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/sakshibansalsb/Hiring-Assistant-ChatBot
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
2. **Greeting and Introduction**: The application will greet the user and provide an overview of the process.
3. **Collect Candidate Information**: Fill out the form with the candidate's details, including name, email, phone number, years of experience, desired position, location, and tech stack.
4. **Generate Technical Questions**: Based on the provided tech stack, the application will generate 3 to 5 technical questions.
5. **Answer Questions**: The candidate can answer the questions directly in the application.
6. **Submit Responses**: Once the candidate submits their responses, the application will display the answers and end the conversation.

## Applications

- **Initial Screening**: Automates the initial screening process for tech roles, saving time for recruiters.
- **Technical Assessment**: Provides tailored technical questions based on the candidate's expertise.
- **Candidate Engagement**: Offers a seamless and interactive experience for candidates during the hiring process.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch to your forked repository.
5. Submit a pull request with a detailed description of your changes.

---

**TalentScout Hiring Assistant** is a powerful tool for recruiters looking to streamline their hiring process and engage candidates effectively. By leveraging the capabilities of the Gemini 1.5 Pro model, it provides a dynamic and efficient way to conduct initial screenings for tech roles.

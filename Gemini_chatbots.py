
# python -m streamlit run Gemini.py
import streamlit as st
import pathlib
import textwrap
import PIL.Image

import google.generativeai as genai
from st_chat_message import message


# Function to generate content based on user query


def generate_response(query, model):
    response = model.generate_content(query)
    return response.text


# Main function to run the Streamlit app


def main():
    # Setup Google Generative AI
    genai.configure(api_key='AIzaSyCR_sUCpmj3YStoAe2fYWDXuSAjC2c1Vls')

    # Safety settings
    safety_settings = [
        {
            "category": "HARM_CATEGORY_DANGEROUS",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE",
        },
    ]

    # Initialize Generative Model
    model = genai.GenerativeModel(
        'gemini-pro', safety_settings=safety_settings)

    # Title and description
    st.title("Aully Chatbot")
    st.write("Welcome to the Aully Chatbot! Ask any question and get a response.")

    # For Decor
    message("Hello Aully!", is_user=True)
    message("Hi Buddy")

    # User input for query
    query = st.text_input("Enter your Problem:")

    # Generate response when user submits query
    if st.button("Ask"):
        if query:
            response = generate_response(query, model)
            st.write(response)


# Run the main function to start the Streamlit app
if __name__ == "__main__":
    main()

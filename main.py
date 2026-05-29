import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.title("PS-1 ChatBot App")

# Retrieve the API key (LangChain natively checks for GOOGLE_API_KEY, but we'll adapt to yours)
gemini_api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')

def generate_response(input_text):
    # 2. Initialize the Gemini model correctly using the API key
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.7, 
        google_api_key=gemini_api_key
    )
    
    # 3. Invoke the model and display content
    response = model.invoke(input_text)
    st.info(response.content)

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    #yes
    try: 
        if gemini_api_key:
            if not gemini_api_key.startswith("AIzaSy"):
                st.warning("Please check your Gemini API key format!", icon="⚠️")
            
            if submitted:
                generate_response(text)
        else:
            raise ValueError("No API Key Provided. Please set GEMINI_API_KEY or GOOGLE_API_KEY in your .env file.")
    except Exception as e:
        st.error(f"Error: {e}")
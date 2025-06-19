import requests
import streamlit as st





def get_response():
    #User_input=input("Enter the Text to predict the Emoji from LLAMA 3.2 Model: ")
    
    response = requests.post(
         'http://localhost:11434/api/generate',
         json={
            'model': 'llama3.2:latest',
            'prompt': f"You are a friendly tech assistant for elderly people. {User_input}. Avoid using technical terms unless explained.",
            'stream': False
        }
    )
    return response.json()['response']


st.set_page_config(page_title="Chatbot for Our Digital Literacy Program", page_icon="🧓",layout="centered",initial_sidebar_state='collapsed')
st.header('Ask Question and stay updated in this era of Technology')

User_input=st.text_input("Ask any questions: ")
submit=st.button("Solution")

if submit and User_input.strip():
    with st.spinner("Thinking..."):
        st.write(get_response())
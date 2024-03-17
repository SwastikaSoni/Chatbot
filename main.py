# Bring in streamlit for UI dev
import os
from dotenv import load_dotenv
import streamlit as st

from ibm_watsonx_ai.foundation_models import Model
load_dotenv()
# setup creds
creds = {
    'apikey': os.getenv('API_KEY'),
    'url': 'https://jp-tok.ml.cloud.ibm.com'
}
project_id = os.getenv('PROJECT_ID')
# Create LLM using Langchain
our_model = Model(
    credentials=creds,
    model_id='meta-llama/llama-2-70b-chat',
    params={
        'decoding_method': 'sample',
        'max_new_tokens': 200,
        'temperature': 0.5
    },
    project_id=project_id
)

# Setup the app title
st.title('OUR AI')

# Setup a session state message variable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.markdown(f'<div style="color: blue; font-size: 16px;">USER: {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="color: green; font-size: 16px;">ASSISTANT: {message["content"]}</div>', unsafe_allow_html=True)

# Build a prompt input template to display the prompts
prompt = st.text_input('Pass Your Prompt here')

# If the user hits enter then
if st.button('Send') or prompt:
    if prompt:
        # Display the prompt
        st.markdown(f'<div style="color: blue; font-size: 16px;">USER: {prompt}</div>', unsafe_allow_html=True)
        # Store the user prompt in state
        st.session_state.messages.append({'role': 'user', 'content': prompt})
        generated_text = our_model.generate_text(prompt=prompt)
        st.markdown(f'<div style="color: green; font-size: 16px;">ASSISTANT: {generated_text}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({'role': 'assistant', 'content': generated_text})

import os
import streamlit as st
import dotenv
import google.generativeai as gpt
import requests
from functions import *

# Load environment variables from .env file
dotenv.load_dotenv()

api_keys = []
# Get API keys from environment and split them into a list
api_keys = os.getenv("GOOGLE_API_KEYS").split(" ")

# Debug: Print the API keys to verify they are loaded correctly
print("Loaded API Keys:", api_keys)

def is_quota_exceeded(api_key):
    # Google Gemini Flash API URL (POST request)
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {
        'Content-Type': 'application/json',
    }
    params = {'key': api_key}
    
    # Updated data payload
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "test"
                    }
                ]
            }
        ]
    }
    
    try:
        # Use json= for proper JSON serialization
        response = requests.post(url, headers=headers, params=params, json=data)
        
        # Debug: Log the response details
        print(f"API key {api_key} Response Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        
        # Check if the request is rate-limited (429) or quota-exceeded
        if response.status_code == 429:
            print(f"API key {api_key} has exceeded the rate limit.")
            return True  # Quota is exceeded
        elif response.status_code == 400:
            # Log details if Bad Request (400)
            print(f"API key {api_key} returned 400 Bad Request. Response: {response.json()}")
            return True  # Treat 400 as invalid due to malformed request
        elif response.status_code != 200:
            print(f"API key {api_key} returned error: {response.status_code}")
            return True  # Any non-200 response as an error for now

        return False  # API key is valid

    except Exception as e:
        print(f"An error occurred with API key {api_key}: {str(e)}")
        return True  # Treat any exceptions as failed attempts


def get_valid_api_key():
    # Iterate over the list of API keys and return the first valid one
    for api_key in api_keys:
        if not is_quota_exceeded(api_key):
            return api_key
    
    # If no key is valid, raise an exception or handle it as you wish
    raise Exception("All API keys have exceeded their quotas or returned errors!")

# Get a valid API key to use
try:
    valid_api_key = get_valid_api_key()
    print(f"Using API key: {valid_api_key}")
except Exception as e:
    print(str(e))

# Load environment variables
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

# Update the environment with the new valid API key
os.environ["GOOGLE_API_KEY"] = valid_api_key

# Write changes to .env file
dotenv.set_key(dotenv_file, "GOOGLE_API_KEY", os.environ["GOOGLE_API_KEY"])

# Fetch and print the stored key for verification
api_key_stored = os.getenv("GOOGLE_API_KEY")
print(f"Stored API key: {api_key_stored}")

# Configure GPT (replace 'gpt' with your appropriate client or method)
gpt.configure(api_key=api_key_stored)


# Configure Streamlit page settings
st.set_page_config(
    page_title="Evolvify Chat",
    page_icon=":robot_face:",  # Favicon emoji
    layout="wide",  # Page layout option
)

API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gpt.configure(api_key=API_KEY)
model = gpt.GenerativeModel('gemini-1.5-flash')

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🤖 Chat with Evolvify bot!")

# Display the chat history
for msg in st.session_state.chat_session.history:
    with st.chat_message(map_role(msg["role"])):
        st.markdown(msg["content"])

# Input field for user's message
user_input = st.chat_input("Ask Evolvify bot...")
if user_input:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_input)

    # Send user's message to Gemini and get the response
    gemini_response = fetch_gemini_response(user_input)

    # Display Gemini's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response)

    # Add user and assistant messages to the chat history
    st.session_state.chat_session.history.append({"role": "user", "content": user_input})
    st.session_state.chat_session.history.append({"role": "model", "content": gemini_response})
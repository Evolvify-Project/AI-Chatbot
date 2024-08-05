# Chatbot Application using Gemini API
## Overview
This project is a chatbot application using the Google Generative AI model (Gemini-Pro) integrated with Streamlit. The chatbot,is designed to interact with users by responding to their questions using advanced generative AI capabilities.

## Features
1. Interactive chatbot interface built with Streamlit
2. Integration with Google Generative AI model (Gemini-Pro)
3. Maintains chat history across user interactions
4. Simple and user-friendly design

## Prerequisites
1. Python 3.8 or higher
2. An API key for the Google Generative AI model

## Installation
1. Clone the repository
``` bash
git clone https://github.com/Gayathri-Selvaganapathi/chatbot_repo.git
cd chatbot-repo
```

2. Set up the virtual environment
Use conda to create a virtual environment based on the environment.yml file:


```bash
conda env create -f environment.yml
conda activate chatbot-env
```

Alternatively, use pip to install the dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```

3. Environment Variables
Create a .env file in the project root directory and add your Google API key:

Get the api key from google ai studio:https://aistudio.google.com/app/apikey

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## Start Steamlit application 

1. Run the application
Execute the Streamlit application:

```bash
streamlit run app.py
```

2. Interact with Gemini-Pro
Open your web browser and navigate to http://localhost:8501. You will see the chat interface where you can start interacting with Gemini-Pro by typing your questions.

## File Structure
1. app.py: Main application file containing the Streamlit interface and logic for the chatbot.
2. functions.py: Helper functions for interacting with the Google Generative AI model.
3. requirements.txt: List of Python dependencies.
4. environment.yml: Conda environment configuration file.
5. .env: File containing environment variables (e.g., Google API key).

Contributing
If you want to contribute to this project, please fork the repository and submit a pull request. You can also open issues for any bugs or feature requests.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

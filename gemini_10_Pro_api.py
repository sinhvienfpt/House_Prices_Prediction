# Get the API key from here: https://ai.google.dev/tutorials/setup
# Create a new secret called "GEMINI_API_KEY", via Add-ons/Secrets in the top menu, and attach it to this notebook

import google.generativeai as genai
from kaggle_secrets import UserSecretsClient

user_secrets = UserSecretsClient()
api_key = user_secrets.get_secret("GEMINI_API_KEY")
genai.configure(api_key = api_key)

# Generate content
model = genai.GenerativeModel(model_name='gemini-pro')
response = model.generate_content('Tell me a story about a magic backpack.')
print(response.text)

# Chat
chat = model.start_chat()
response = chat.send_message('Hi, I have some questions for you.')
print(response.text)
response = chat.send_message('What is the weather today?')
print(response.text)

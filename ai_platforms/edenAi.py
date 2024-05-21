import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {"Authorization": os.environ.get("EDENAI_KEY")}


url = "https://api.edenai.run/v2/text/chat"

assistant = "Acts as an blog generator assitant /n your job is to get the title and create blog related to that topic /n make the content of blog about 250 words /n give the suitable title for that blog /n if possible give a suitable real time event as example"

text = input("Enter any title: ")

payload = {
    "providers": "openai",
    "text": text,
    "chatbot_global_action": assistant,
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "google,amazon"
}

response = requests.post(url, json=payload, headers=headers)

result = json.loads(response.text)
print(result['openai']['generated_text'])

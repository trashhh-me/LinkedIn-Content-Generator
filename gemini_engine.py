# gemini_engine.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("Gemini_API_Key")

def generate_post(prompt):
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"❌ Error: {response.status_code} - {response.text}"
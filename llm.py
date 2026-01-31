import os
import requests

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",   # required by OpenRouter
    "X-Title": "AcademicTwin"
}

def chatbot_response(user_message):

    try:
        payload = {
            "model": "tngtech/deepseek-r1t-chimera:free",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful academic assistant. Give practical study advice in simple language."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)

        if r.status_code != 200:
            return f"OpenRouter HTTP {r.status_code}: {r.text}"

        data = r.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"OpenRouter crash >>> {e}"
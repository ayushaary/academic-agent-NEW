import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def chatbot_response(prompt):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "tngtech/deepseek-r1t-chimera:free",
        "messages": [
            {"role": "system", "content": "You are an academic assistant helping students improve study habits and GPA."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,     # <<< IMPORTANT
        "temperature": 0.7
    }

    try:
        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )

        return res.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ OpenRouter error: {e}"

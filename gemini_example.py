import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def query_gemini(prompt):

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"API Error {response.status_code}: {response.text}"

    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Gemini...")

    result = query_gemini(user_prompt)

    print("Response:")
    print(result)
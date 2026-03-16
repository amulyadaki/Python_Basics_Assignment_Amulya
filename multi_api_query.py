import os
import requests
from dotenv import load_dotenv
import cohere

load_dotenv()

# API KEYS
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

co = cohere.Client(COHERE_API_KEY)


# ---------------- GROQ ----------------
def query_groq(prompt):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }

    r = requests.post(url, headers=headers, json=data)

    if r.status_code != 200:
        return f"Error {r.status_code}"

    return r.json()["choices"][0]["message"]["content"]


# ---------------- HUGGINGFACE ----------------
def query_huggingface(prompt):

    url = "https://router.huggingface.co/hf-inference/models/distilgpt2"

    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
    }

    payload = {"inputs": prompt}

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code != 200:
        return f"Error {r.status_code}"

    data = r.json()

    if isinstance(data, list):
        return data[0].get("generated_text")

    return str(data)


# ---------------- COHERE ----------------
def query_cohere(prompt):

    try:
        response = co.chat(
            model="command-r-plus-08-2024",
            message=prompt
        )

        return response.text

    except Exception as e:
        return str(e)


# ---------------- GEMINI ----------------
def query_gemini(prompt):

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GOOGLE_API_KEY}"

    headers = {"Content-Type": "application/json"}

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    r = requests.post(url, headers=headers, json=data)

    if r.status_code != 200:
        return f"Error {r.status_code}"

    result = r.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]


# ---------------- OLLAMA ----------------
def query_ollama(prompt):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        r = requests.post(url, json=data)

        if r.status_code != 200:
            return f"Error {r.status_code}"

        return r.json()["response"]

    except:
        return "Ollama not running"


# ---------------- MAIN ----------------

if __name__ == "__main__":

    prompt = input("Enter your prompt: ")

    print("\nQuerying APIs...\n")

    print("----- GROQ -----")
    print(query_groq(prompt))

    print("\n----- HUGGINGFACE -----")
    print(query_huggingface(prompt))

    print("\n----- COHERE -----")
    print(query_cohere(prompt))

    print("\n----- GEMINI -----")
    print(query_gemini(prompt))

    print("\n----- OLLAMA -----")
    print(query_ollama(prompt))
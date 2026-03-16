import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=API_KEY
)

prompt = input("Enter your prompt: ")

print("Querying HuggingFace...")

response = client.chat_completion(
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

print("Response:")
print(response.choices[0].message["content"])
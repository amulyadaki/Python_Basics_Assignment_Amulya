import os
import cohere
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.ClientV2(API_KEY)

prompt = input("Enter your prompt: ")

print("Querying Cohere...")

response = co.chat(
    model="command-a-03-2025",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("Response:")
print(response.message.content[0].text)
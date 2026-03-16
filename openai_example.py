import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = input("Enter your prompt: ")

print("Querying OpenAI...")

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", str(e))
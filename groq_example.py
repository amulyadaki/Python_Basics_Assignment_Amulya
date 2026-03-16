import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)


def query_groq(prompt):
    """
    Send prompt to Groq Llama model
    """

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":

    prompt = input("Enter your prompt: ")

    print("Querying Groq...")

    result = query_groq(prompt)

    print("\nResponse:\n")
    print(result)
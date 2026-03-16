import requests

url = "http://localhost:11434/api/generate"

def query_ollama(prompt):

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data, timeout=120)

        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text}"

        result = response.json()

        return result.get("response", "No response received")

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":

    user_prompt = input("Enter your prompt: ")

    print("Querying Ollama...")

    result = query_ollama(user_prompt)

    print("\nResponse:")
    print(result)
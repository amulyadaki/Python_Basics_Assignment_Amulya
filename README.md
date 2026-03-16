# AI API Integration Assignment

## Overview

This project demonstrates how to integrate multiple Generative AI APIs using Python.
The goal of the assignment is to understand how different AI providers can be accessed programmatically and how prompts can be sent to generate responses.

In this project, Python scripts were created to connect with different AI APIs, send prompts, and display the generated responses.

---

## APIs Used

The following AI APIs were integrated:

* OpenAI API
* Groq API
* HuggingFace API
* Google Gemini API
* Cohere API
* Ollama (Local LLM)
* Multi API Query

Each API was tested with a sample prompt and the response was displayed in the terminal.

---

## Project Structure

```
ai-api-integration
│
├── openai_example.py
├── groq_example.py
├── huggingface_example.py
├── gemini_example.py
├── cohere_example.py
├── ollama_example.py
├── multi_api_query.py
├── requirements.txt
├── README.md
│
└── screenshots
    ├── openai_output.png
    ├── groq_output.png
    ├── huggingface_output.png
    ├── gemini_output.png
    ├── cohere_output.png
    ├── ollama_output.png
    └── multiapiquery_output.png

```

---

## Installation

Clone the repository:

```
git clone https://github.com/amulyadaki/Python_Basics_Assignment_Amulya.git
```

Navigate to the project folder:

```
cd ai-api-integration
```

Install the required dependencies:

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project folder and add your API keys:

```
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
GOOGLE_API_KEY=your_gemini_api_key
COHERE_API_KEY=your_cohere_api_key
```

---

## Running the Programs

Run each Python file to test the APIs.

Example:

```
python openai_example.py
```

After running the script, enter a prompt when asked and the AI will generate a response.

Example prompt:

```
What is Artificial Intelligence?
```

---

## Screenshots

### OpenAI API Output
![OpenAI Output](screenshots/openai_output.png)

### Groq API Output
![Groq Output](screenshots/groq_output.png)

### HuggingFace API Output
![HuggingFace Output](screenshots/huggingface_output.png)

### Gemini API Output
![Gemini Output](screenshots/gemini_output.png)

### Cohere API Output
![Cohere Output](screenshots/cohere_output.png)

### Ollama Output
![Ollama Output](screenshots/ollama_output.png)

### Multi API Query Output
![Multi API Output](screenshots/multiapiquery_output.png)
## Technologies Used

* Python
* OpenAI API
* Groq API
* HuggingFace API
* Google Gemini API
* Cohere API
* Ollama
* Requests Library
* python-dotenv

---

## Conclusion

This assignment helped in understanding how different AI APIs can be integrated into Python applications. It also demonstrated how prompts can be sent to AI models and how responses can be processed and displayed.

---

## Author

Amulya Daki
AI & Python Assignment

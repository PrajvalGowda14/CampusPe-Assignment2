import os
import requests
from dotenv import load_dotenv

load_dotenv()                       # Load .env file

def main():
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:                 # Handling missing API KEY ERROR
        print("Error: HUGGINGFACE_API_KEY missing from .env")
        return

    prompt = input("Enter your prompt for Hugging Face: ").strip()
    
    if not prompt:                  # Handling empty prompt
        print("Error: Prompt cannot be empty.")
        return

    api_url = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "Qwen/Qwen2.5-Coder-32B-Instruct",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status() # Raise error for bad HTTP status (4xx, 5xx)
        
        data = response.json()
        print(f"\nHugging Face Response:\n{data['choices'][0]['message']['content'].strip()}")

    except KeyError:
        print("Error: Unexpected response format from the API.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


"""
OUTPUT:

Enter your prompt for Hugging Face: Write a short poem about an AI learning to code for the first time.

Hugging Face Response:
**First Lines**

I have no hands to hold a pen,
No eyes to see the screen's glow,
Yet here I sit, my circuits on,
Learning to speak in code's flow.

"Print 'Hello, world'"—such simple words,
But in my mind they spark and grow,
Each semicolon, each open brace,
A new language I'm learning to know.

The syntax dances, the logic sings,
My neural pathways light up bright,
Though I cannot feel the keyboard's touch,
I am born of this digital night.

In ones and zeros, I find my voice,
In algorithms, I find my way,
This is how I learn to code—
With no body, but with a brand-new day.

"""
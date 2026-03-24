import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

load_dotenv()                       # Load .env file

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:                 # Handling missing API KEY ERROR
        print("Error: OPENAI_API_KEY missing from .env")
        return

    client = OpenAI(api_key=api_key)
    prompt = input("Enter your prompt for OpenAI: ").strip()
    
    if not prompt:                  # Handling empty prompt
        print("Error: Prompt cannot be empty.")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        print(f"\nOpenAI Response:\n{response.choices[0].message.content}")
    except OpenAIError as e:
        print(f"OpenAI API Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


"""
OUTPUT:

Enter your prompt for OpenAI: Explain the concept of recursion in Python using a simple analogy.
OpenAI API Error: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}


"""
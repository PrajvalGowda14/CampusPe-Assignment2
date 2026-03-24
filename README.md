Name: Prajval Gowda
Questions Attempted: 1 - 20

Special Instructions: 

Nothing really, everything is pretty straight forward. have output in the files itself.

Challenges faced:

1. ALIGNMENT: Aligning the right border (║) in the boxed formatting was difficult when variable lengths changed. Solved this by converting values to strings and using " " * (width - length) math. Also used ^ for center align formatting

2. Age Calculator: Had to use new package and learn new logic to build the program.

3. Print formatting: Took more time to make output look prettier than building the logic itself.

4. Edge cases: finding edge cases and fixing bugs accordingly(not a big challenge).


# ASSIGNMENT 2
# AI API Integration - Gen AI Task

## Project Objective
This project integrates six different Generative AI providers into individual Python programs. It demonstrates secure API key management using environment variables and robust error handling.

## Integrated Providers
1. **OpenAI** (gpt-4o-mini)
2. **Groq** (llama-3.1-8b-instant)
3. **Ollama** (Local Llama3)
4. **Hugging Face** (Qwen2.5-Coder-32B-Instruct)
5. **Google Gemini** (gemini-2.5-flash)
6. **Cohere** (command-r-08-2024)

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory and add your keys:
   ```env
   OPENAI_API_KEY=your_key
   GROQ_API_KEY=your_key
   HF_TOKEN=your_token
   GOOGLE_API_KEY=your_key
   COHERE_API_KEY=your_key
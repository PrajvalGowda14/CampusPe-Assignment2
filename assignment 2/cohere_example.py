import os
import cohere
from dotenv import load_dotenv

# Load environment variables from .env [cite: 40, 54]
load_dotenv()

def main():
    # Retrieve the API key from environment variables [cite: 40]
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        print("Error: COHERE_API_KEY not found in .env file.")
        return

    # Initialize the Cohere client [cite: 20]
    # Note: Trial keys are limited to 20 calls per minute
    co = cohere.Client(api_key=api_key)
    
    # Accept user input (prompt) [cite: 33]
    prompt = input("Enter your prompt for Cohere: ").strip()
    if not prompt:
        print("Error: Prompt cannot be empty.")
        return

    try:
        # Use the Chat API with a stable versioned model 
        response = co.chat(
            message=prompt,
            model="command-r-08-2024" 
        )
        
        # Display the response [cite: 35]
        print(f"\nCohere Response:\n{response.text}")

    except Exception as e:
        # Handle errors gracefully as per assignment requirements [cite: 35, 70]
        print(f"An error occurred with the Cohere API: {e}")
        print("Tip: If you see a '429' error, you've hit the Trial Key rate limit. Wait 60 seconds.")

if __name__ == "__main__":
    main()



"""
OUTPUT: 
Enter your prompt for Cohere: Summarize the importance of using environment variables for API keys.

Cohere Response:
Environment variables are a crucial tool for managing sensitive information, such as API keys, in a secure and controlled manner. Here's why they are important:

1. **Security**: Storing API keys as environment variables keeps them out of the codebase, reducing the risk of accidental exposure. Unlike hardcoded keys, which are directly embedded in the source code, environment variables are separate and can be easily changed without modifying the code. This enhances security by preventing sensitive data from being publicly accessible.

2. **Flexibility and Scalability**: Environment variables allow for easy configuration and management of API keys across different environments, such as development, staging, and production. Developers can set up unique keys for each environment, ensuring that the correct credentials are used in the appropriate context. This flexibility is especially valuable in large-scale projects or when working with multiple teams.

3. **Centralized Control**: By centralizing API keys in environment variables, organizations can maintain better control over their sensitive data. Changes to keys can be made in a single location, ensuring consistency and reducing the chances of errors. This approach also facilitates collaboration, as multiple team members can access and update keys without directly modifying the code.

4. **Version Control and Deployment**: Environment variables are often excluded from version control systems, ensuring that API keys do not accidentally get committed to a repository. This practice maintains confidentiality and simplifies the deployment process, as developers can focus on the code without worrying about sensitive data.

5. **Dynamic Configuration**: Environment variables enable dynamic configuration, allowing developers to easily switch between different API keys or configurations based on the environment or specific use cases. This dynamic nature enhances the adaptability and maintainability of the application.

6. **Best Practice and Industry Standard**: Using environment variables for API keys is a widely adopted best practice in software development. It aligns with security guidelines and industry standards, ensuring that applications are built with security and maintainability in mind.

In summary, environment variables provide a secure, flexible, and controlled way to manage API keys, enhancing the overall security and maintainability of software applications.

"""
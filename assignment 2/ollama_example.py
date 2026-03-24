import requests
import json

def main():
    prompt = input("Enter prompt for Ollama (Llama3): ").strip()
    url = "http://localhost:11434/api/generate"
    payload = {"model": "llama3", "prompt": prompt, "stream": False}
    
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status() # Check for HTTP errors
        print(f"\nOllama Response:\n{response.json().get('response')}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Is the Ollama app running?")
    except Exception as e:
        print(f"Ollama Error: {e}")

if __name__ == "__main__":
    main()




"""
OUTPUT: 
Enter prompt for Ollama (Llama3): Compare the pros and cons of running LLMs locally versus in the cloud.

Ollama Response:
The age-old debate: to run Large Language Models (LLMs) locally or in the cloud? Both approaches have their advantages and disadvantages, which I'll outline below:

**Running LLMs Locally**

Pros:

1. **Control and customization**: When you run an LLM locally, you have complete control over the model's configuration, hyperparameters, and training data.
2. **Security and compliance**: By hosting the model on your own premises, you can ensure that sensitive data remains within your organization's secure environment.
3. **Faster access to results**: With a local installation, you can access the model's output in near-real-time, without relying on cloud connectivity or latency.
4. **No dependency on internet connectivity**: Your LLM will continue to function even when internet connectivity is lost.

Cons:

1. **Hardware requirements**: Running an LLM locally requires significant computational resources (e.g., NVIDIA GPUs) and memory, which can be a barrier for smaller organizations or individuals.
2. **Maintenance and updates**: You'll need to handle model updates, maintenance, and scaling, which can be time-consuming and require specialized expertise.
3. **Limited scalability**: Local installations may not be able to scale as easily as cloud-based solutions, which can limit the size and complexity of your projects.

**Running LLMs in the Cloud**

Pros:

1. **Scalability and flexibility**: Cloud services like Google Colab, AWS SageMaker, or Azure Machine Learning offer scalable infrastructure that can handle large models and complex tasks.
2. **No hardware requirements**: You don't need to invest in expensive hardware or maintain a data center, as cloud providers take care of the infrastructure.
3. **Access to pre-trained models**: Cloud services often provide access to pre-trained LLMs, which can save you time and computational resources for training your own models.
4. **Collaboration and sharing**: Cloud-based solutions facilitate collaboration with other researchers or developers by allowing easy sharing and version control.

Cons:

1. **Dependence on internet connectivity**: Your cloud-based LLM is only as good as your internet connection, which can be unreliable or slow in some areas.
2. **Security concerns**: Storing sensitive data in the cloud may raise security concerns, as you're relying on third-party providers to keep your data secure.
3. **Cost and budget constraints**: Cloud services can be expensive, especially if you need to run large models or complex tasks for extended periods.
4. **Limited customization**: While cloud services offer flexibility, they may not allow the same level of customization and control as running an LLM locally.

In conclusion, running LLMs locally is ideal when:

* You have specific requirements that can't be met by cloud providers (e.g., custom hyperparameters or sensitive data).
* You need fast access to results without relying on internet connectivity.
* You're working with small to medium-sized datasets and don't require significant scalability.

On the other hand, running LLMs in the cloud is suitable when:

* You need scalable infrastructure for large models or complex tasks.
* You want to take advantage of pre-trained models and access to shared knowledge.
* You prioritize flexibility and collaboration over customization and control.

Ultimately, the choice between running LLMs locally or in the cloud depends on your specific project requirements, budget constraints, and organizational priorities.


"""
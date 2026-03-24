import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()                           # Load .env file

def main():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:                     # Handling missing API KEY ERROR
        print("Error: GROQ_API_KEY missing from .env")
        return
    
    client = Groq(api_key=api_key)
    prompt = input("Enter your prompt for Groq: ").strip()
    if not prompt:                      # Handling empty prompt
        print("Error: Prompt cannot be empty.")
        return

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        print(f"\nGroq Response:\n{completion.choices[0].message.content}")
    except Exception as e:
        print(f"Groq Error: Verify your API key or Rate Limits. Details: {e}")

if __name__ == "__main__":
    main()


"""
OUTPUT:

Enter your prompt for Groq: Write a high-performance Python function to find the factorial of a number.

Groq Response:
**High-Performance Factorial Function in Python**

To achieve high performance, we'll use memoization to store previously calculated factorials. This will prevent redundant calculations and significantly improve the function's speed for larger input values.

```python
def factorial(n):
    # Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Initialize a dictionary to store memoized results
    memo = {0: 1}

    def factorial_helper(n):
        # If the result is already memoized, return it
        if n in memo:
            return memo[n]

        # Calculate the result and store it in memo
        result = n * factorial_helper(n-1)
        memo[n] = result
        return result

    # Call the helper function and return the result
    return factorial_helper(n)
```

**Example Usage:**

```python
print(factorial(5))  # Output: 120
print(factorial(10))  # Output: 3628800
```

**Time Complexity:**

The time complexity of this function is O(n), which is a significant improvement over the naive recursive approach, which has a time complexity of O(n!) due to redundant calculations.

**Tips for Optimization:**

1.  **Use Iterative Approach:** While the recursive approach is often more elegant, it can be slower due to the overhead of function calls. Consider using an iterative approach with a loop to calculate the factorial.
2.  **Choose the Right Data Structure:** For large inputs, consider using a data structure like `numpy` or `array` to store the memoized results. These data structures are more memory-efficient and can provide faster access times.
3.  **Consider Parallelism:** For extremely large inputs, you can take advantage of parallel processing to calculate the factorial. You can divide the input into smaller chunks and calculate them in parallel using libraries like `multiprocessing` or ` joblib`.

"""
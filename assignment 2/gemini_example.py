import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found.")
        return

    genai.configure(api_key=api_key)
    prompt = input("Enter your prompt for Gemini: ").strip()
    
    if not prompt:
        print("Error: Prompt cannot be empty.")
        return

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        if response.text:
            print(f"\nGemini Response:\n{response.text}")
        else:
            print("Gemini returned an empty response (possibly blocked content).")
    except Exception as e:
        print(f"Gemini Error: {e}")

if __name__ == "__main__":
    main()



"""
OUTPUT:
FutureWarning: 

All support for the `google.generativeai` package has ended. It will no longer be receiving 
updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
See README for more details:

https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md

  import google.generativeai as genai
Enter your prompt for Gemini: List three main differences between a list and a tuple in Python.

Gemini Response:
Here are three main differences between a list and a tuple in Python:

1.  **Mutability:**
    *   **List:** Lists are **mutable**, meaning you can change, add, or remove elements after the list has been created.
        *   *Example:* `my_list = [1, 2, 3]`; `my_list.append(4)`; `my_list[0] = 10`
    *   **Tuple:** Tuples are **immutable**, meaning their contents cannot be changed after creation. You cannot add, remove, or modify elements in a tuple. If you need a "modified" tuple, you must create a new one.
        *   *Example:* `my_tuple = (1, 2, 3)`; `my_tuple[0] = 10` would raise a `TypeError`.

2.  **Use Cases and Purpose:**
    *   **List:** Lists are typically used for collections of items that might change during the program's execution, or when the order of items is important and elements are often homogeneous (of the same type). They represent a sequence of data.
        *   *Example:* A shopping list, a list of users, a series of measurements.
    *   **Tuple:** Tuples are often used for fixed collections of items, especially when the items represent a "record" or a collection of related but possibly heterogeneous data (different types) that belongs together and shouldn't be altered. They represent a fixed data structure.
        *   *Example:* Coordinates `(x, y)`, an RGB color `(red, green, blue)`, a database record `('John Doe', 30, 'New York')`.

3.  **Performance, Memory & Hashing:**
    *   **List:** Because lists are mutable, they generally require slightly more memory (due to overhead for managing potential changes) and might be marginally slower for certain operations (though this is often negligible for typical use cases). Crucially, **lists cannot be hashed**, which means they cannot be used as keys in dictionaries or as elements in sets.
    *   **Tuple:** Because tuples are immutable, Python can perform certain optimizations. They generally consume slightly less memory and can sometimes be marginally faster to process. Most importantly, **tuples can be hashed** (provided all their elements are also hashable), allowing them to be used as keys in dictionaries (`dict`) and elements in sets (`set`).
        *   *Example (Hashing):* `my_dict = {('a', 'b'): 1}` is valid, but `my_dict = {['a', 'b']: 1}` would raise a `TypeError`.

"""
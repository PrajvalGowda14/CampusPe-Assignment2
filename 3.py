"""
Question 3: String Manipulator
"""


sentence = input("Enter a sentence: ")

# list of words
words = sentence.split()

print(f"Original: {sentence}")
print(f"Characters (with spaces): {len(sentence)}")
print(f"Characters (without spaces): {len(sentence) - sentence.count(' ')}")
print(f"Words: {len(words)}")
print(f"UPPERCASE: {sentence.upper()}")
print(f"lowercase: {sentence.lower()}")
print(f"Title Case: {sentence.title()}")

# used list indexing to get first and last words
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")

# used string slicing to reverse sentence
print(f"Reversed: {sentence[::-1]}")



"""
OUTPUT:

Enter a sentence: Hello World Python 
Original: Hello World Python
Characters (with spaces): 18
Characters (without spaces): 16
Words: 3
UPPERCASE: HELLO WORLD PYTHON
lowercase: hello world python
Title Case: Hello World Python
First word: Hello
Last word: Python
Reversed: nohtyP dlroW olleH

"""
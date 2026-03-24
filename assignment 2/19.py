"""
Question 19: Text Analysis Functions
"""


from collections import Counter

def count_words(text):
    return len(text.split())

def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def count_consonants(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in vowels:              # checks all the characters which are not vowels
            count += 0

    return count

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    text_list = text.lower().split()
    cleaned = "".join(text_list)
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    new_text = ""
    for char in text:                   # create a new string and add non vowels only
        if char not in vowels:
            new_text += char
    return new_text

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        word = word.strip(".,!?")       # cleaning punctuation from words
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def longest_word(text):
    words = text.split()
    max_len = 0
    if not words:
        return ""
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest = word

    return f"{longest} ({len(longest)} letters)"

def analyze_text():
    width = 35
    # using eval to stay consistent with your previous inputs
    inp = input("Enter text: ")
    
    print("\n" + "═" * width)
    print(f"{'TEXT ANALYSIS':^{width}}")
    print("═" * width)
    
    # calling all functions and printing results
    print(f"Words          : {count_words(inp)}")
    print(f"Vowels         : {count_vowels(inp)}")
    print(f"Consonants     : {count_consonants(inp)}")
    print(f"Reversed       : {reverse_text(inp)}")
    print(f"Palindrome     : {'Yes' if is_palindrome(inp) else 'No'}")
    print(f"Without vowels : {remove_vowels(inp)}")
    print(f"Longest word   : {longest_word(inp)}")
    
    # formatting word frequency dictionary as a string
    freq = word_frequency(inp)
    freq_str = ", ".join([f"{k}: {v}" for k, v in freq.items()])
    print(f"Word Frequency : {freq_str}")
    
    print("═" * width)

# running the analysis
analyze_text()

"""
OUTPUT:

Enter text: Hello World Hello

═══════════════════════════════════
           TEXT ANALYSIS
═══════════════════════════════════
Words          : 3
Vowels         : 5
Consonants     : 0
Reversed       : olleH dlroW olleH
Palindrome     : No
Without vowels : Hll Wrld Hll
Longest word   : Hello (5 letters)
Word Frequency : hello: 2, world: 1
═══════════════════════════════════

"""
"""
Question 15: Prime Number Checker
"""

import math

# Part 1: Check if a single number is prime
num = int(input("Enter a number: "))

def is_prime(num):
    if num <= 1:                # handling non prime 0, 1 and negative numbers
        return False
    
    is_prime_ = True
    for i in range(2, int(num**0.5) + 1):       # check for factors from 2 up to root of the number
        if num % i == 0:
            is_prime_ = False

    return is_prime_


# print result for part 1
if is_prime(num):
    print(f"{num} is a PRIME number")
else:
    print(f"{num} is NOT a prime number")


# Part 2: Find all prime numbers in a given range
start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

prime_list = []

# Loop through the range
for n in range(start, end + 1):
    if n > 1:
        # Check if n is prime and add it to the list
        if is_prime(n):
            prime_list.append(str(n))

# Print result for Part 2
print(f"Prime numbers: {', '.join(prime_list)}")



"""
OUTPUT:

Enter a number: 17
17 is a PRIME number

Enter start range: 1
Enter end range: 30
Prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

"""
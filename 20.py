"""
Question 20: Number System Functions
"""

# Required Mathematical Functions
def factorial(n):
    fact = 1
    for i in range(1, n + 1):           # even works for 0, 1
        fact *= i
    return fact

def is_prime(n):
    if n <= 1:                          # handling 0, 1, nengative numbers
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: 
            return False
    return True

def fibonacci(n):
    if n <= 0: 
        return 0
    elif n == 1: 
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b                        # 0 1 1 2 3 5 8 13 21 34 .....

def sum_of_digits(n):
    text = str(abs(n))
    total = 0
    for x in text:
        total += int(x)
    return total

def reverse_number(n):
    rev = str(abs(n))[::-1]
    return int(rev) * (-1 if n < 0 else 1)

def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]
    power = len(digits)
    return sum(d**power for d in digits) == abs(n)

def gcd(a, b):                      #  find the remainder of the numbers until it becomes zero
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):                      # lcm = a * b / hcf
    if a == 0 or b == 0: 
        return 0
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    if n <= 1: 
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Main menu function
def math_menu():
    width = 35
    while True:
        print("\n" + "═" * width)
        print(f"{'NUMBER SYSTEM FUNCTIONS':^{width}}")
        print("═" * width)
        print("1. Factorial (n!)           6. Armstrong Check")
        print("2. Prime Check              7. GCD (a, b)")
        print("3. Fibonacci (nth)          8. LCM (a, b)")
        print("4. Sum of Digits            9. Perfect Number")
        print("5. Reverse Number          10. Exit")
        print("═" * width)

        choice = input("Enter choice (1-10): ")
        if choice == '10': 
            print("Exiting ...")
            break

        # single input operations
        if choice in ['1', '2', '3', '4', '5', '6', '9']:
            num = eval(input("Enter number (n): "))
            if choice == '1': print(f"Result: {factorial(num)}")
            elif choice == '2': print(f"Is Prime: {is_prime(num)}")
            elif choice == '3': print(f"Fibonacci({num}): {fibonacci(num)}")
            elif choice == '4': print(f"Sum of digits: {sum_of_digits(num)}")
            elif choice == '5': print(f"Reversed: {reverse_number(num)}")
            elif choice == '6': print(f"Is Armstrong: {is_armstrong(num)}")
            elif choice == '9': print(f"Is Perfect: {is_perfect_number(num)}")
        
        # double input operations
        elif choice in ['7', '8']:
            a = eval(input("Enter first number (a): "))
            b = eval(input("Enter second number (b): "))
            if choice == '7': print(f"GCD of {a}, {b}: {gcd(a, b)}")
            elif choice == '8': print(f"LCM of {a}, {b}: {lcm(a, b)}")
        else:
            print("Invalid choice!")

# run the menu
math_menu()



"""
OUTPUT:

═══════════════════════════════════
      NUMBER SYSTEM FUNCTIONS
═══════════════════════════════════
1. Factorial (n!)           6. Armstrong Check
2. Prime Check              7. GCD (a, b)
3. Fibonacci (nth)          8. LCM (a, b)
4. Sum of Digits            9. Perfect Number
5. Reverse Number          10. Exit
═══════════════════════════════════
Enter choice (1-10): 6
Enter number (n): 153
Is Armstrong: True

═══════════════════════════════════
      NUMBER SYSTEM FUNCTIONS
═══════════════════════════════════
1. Factorial (n!)           6. Armstrong Check
2. Prime Check              7. GCD (a, b)
3. Fibonacci (nth)          8. LCM (a, b)
4. Sum of Digits            9. Perfect Number
5. Reverse Number          10. Exit
═══════════════════════════════════
Enter choice (1-10): 9 
Enter number (n): 6
Is Perfect: True

═══════════════════════════════════
      NUMBER SYSTEM FUNCTIONS
═══════════════════════════════════
1. Factorial (n!)           6. Armstrong Check
2. Prime Check              7. GCD (a, b)
3. Fibonacci (nth)          8. LCM (a, b)
4. Sum of Digits            9. Perfect Number
5. Reverse Number          10. Exit
═══════════════════════════════════
Enter choice (1-10): 3
Enter number (n): 8
Fibonacci(8): 21

═══════════════════════════════════
      NUMBER SYSTEM FUNCTIONS
═══════════════════════════════════
1. Factorial (n!)           6. Armstrong Check
2. Prime Check              7. GCD (a, b)
3. Fibonacci (nth)          8. LCM (a, b)
4. Sum of Digits            9. Perfect Number
5. Reverse Number          10. Exit
═══════════════════════════════════
Enter choice (1-10): 1
Enter number (n): 5
Result: 120

"""
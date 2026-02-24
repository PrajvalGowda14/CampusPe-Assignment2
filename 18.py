"""
Question 18: Calculator Functions
"""


# calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # handle division by zero
    if b == 0:
        return "Error (Div by 0)"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

# main function with menu
def calculator():
    width = 30
    
    while True:
        # printing menu
        print("\n" + "═" * width)
        print(f"{'FUNCTION CALCULATOR':^{width}}")
        print("═" * width)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (^)")
        print("7. Exit")
        print("═" * width)

        choice = input("Enter choice (1-7): ")

        if choice == '7':
            print("Exiting...")
            break
            
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = eval(input("Enter first number: "))
            num2 = eval(input("Enter second number: "))
            
            result = 0
            op = ""             # sign for printing

            # calling appropriate function
            if choice == '1':
                result = add(num1, num2)
                op = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                op = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                op = "*"
            elif choice == '4':
                result = divide(num1, num2)
                op = "/"
            elif choice == '5':
                result = modulus(num1, num2)
                op = "%"
            elif choice == '6':
                result = power(num1, num2)
                op = "^"

            # printing result
            print("\n" + "═" * width)
            print(f"Equation: {num1} {op} {num2}")
            print(f"Result  : {result}")
            print("═" * width)
        else:
            print("Invalid choice! Try again.")

# call calculator function to start the prog
calculator()



"""
OUTPUT:

══════════════════════════════
     FUNCTION CALCULATOR
══════════════════════════════
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Power (^)
7. Exit
══════════════════════════════
Enter choice (1-7): 5
Enter first number: 5
Enter second number: 2

══════════════════════════════
Equation: 5 % 2
Result  : 1
══════════════════════════════

MENU

Enter choice (1-7): 6
Enter first number: 2
Enter second number: 8

══════════════════════════════
Equation: 2 ^ 8
Result  : 256
══════════════════════════════

MENU

Enter choice (1-7): 8
Invalid choice! Try again.

MENU

Enter choice (1-7): 7
Exiting...

"""
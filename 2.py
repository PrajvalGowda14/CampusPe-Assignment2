"""
Question 2: Simple Calculator
"""


num1 = eval(input("Enter first number: "))              #used eval to avoid the default string and pick suitable variable type
num2 = eval(input("Enter second number: "))             #float would give decimal values for normal int. decimal input for int type would throw an error

# print(type(num1), type(num2))                         for debugging

print("Results:")

# calculation and printing
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {round(num1 / num2, 2)}")     #used round to get only 2 decimal points
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ^ {num2} = {num1 ** num2}")



"""
OUTPUT:

Enter first number: 10
Enter second number: 3
Results:
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
10 % 3 = 1
10 ^ 3 = 1000

"""
"""
Question 14: Factorial Calculator
"""



# input
num = int(input("Enter a number: "))
width = num * 6

print("\n" + "═" * width)

if num < 0:                     # handling negative numbers
    print("Error: Factorial not defined for negative numbers.")

elif num == 0 or num == 1:      # handling 0 and 1
    print(f"{num}! = 1")

else:                           # calculating factorial using a loop
    fact = 1
    steps = ""                  # string of steps for printing
    
    # loop from num down to 1
    for i in range(num, 0, -1):
        fact *= i
        if i == 1:              # last digit
            steps += str(i)
        else:                   # add 5 x to the string ...
            steps += f"{i} x "
            
    # printing the final step by step result
    print(f"{num}! = {steps} = {fact}")

print("═" * width)

"""
OUTPUT:

Enter a number: 5

══════════════════════════════
5! = 5 x 4 x 3 x 2 x 1 = 120
══════════════════════════════
"""

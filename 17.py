"""
Question 17: Palindrome Checker
"""


width = 30

# input string or number to check for palindrome
inp = str(input("Enter word/number: "))

original = inp
cleaned = inp.lower()           # convert to lowercase (for ignore case)

print("\n" + "═" * width)
print(f"Original: {original}")
print(f"Reversed: {original[::-1]}")
print("-" * width)

# step-by-step verification loop
print("Verifying characters:")
is_palindrome = True

n = len(cleaned)

for i in range(int(n/2)+1):
    a = cleaned[i]
    b = cleaned[n-i-1]
    
    if a == b:
        print(f"  {a} == {b} [Match]")
    else:
        print(f"  {a} != {b} [No Match]")
        is_palindrome = False
        break

print("-" * width)

# final result
if is_palindrome:
    result = "PALINDROME"
else:
    result = "NOT A PALINDROME"

print(f"Result: {result}")
print("═" * width)



"""
OUTPUT:

Enter word/number: RaceCar

══════════════════════════════
Original: RaceCar
Reversed: raCecaR
------------------------------
Verifying characters:
  r == r [Match]
  a == a [Match]
  c == c [Match]
  e == e [Match]
------------------------------
Result: PALINDROME
══════════════════════════════

Enter word/number: 45854

══════════════════════════════
Original: 45854
Reversed: 45854
------------------------------
Verifying characters:
  4 == 4 [Match]
  5 == 5 [Match]
  8 == 8 [Match]
------------------------------
Result: PALINDROME
══════════════════════════════

"""
"""
Question 8: Leap Year Checker
"""

# input year
year = eval(input("Enter a year to check: "))

# check for leap year or not and reason
is_leap = False
reason = ""

# a year is a leap year if it is divisible by 4 and either non divisible by 100 or 400 || or divisible by all 4 and 100 and 400

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
            reason = "Divisible by 4, 100, and 400"
        else:
            is_leap = False
            reason = "Divisible by 4 and 100, but not 400"
    else:
        is_leap = True
        reason = "Divisible by 4 but not 100"
else:
    is_leap = False
    reason = "Not divisible by 4"

# result string for the status
status = "LEAP YEAR" if is_leap else "NOT A LEAP YEAR"

width = 50

# printing status
print("\n" + "═" * width)
print(f"{'LEAP YEAR CHECKER':^{width}}")
print("═" * width)
print(f"Year   : {year}")
print(f"Status : {status}")
print(f"Reason : {reason}")
print("═" * width)

"""

OUTPUT:
Enter a year to check: 2024

══════════════════════════════════════════════════
                LEAP YEAR CHECKER
══════════════════════════════════════════════════
Year   : 2024
Status : LEAP YEAR
Reason : Divisible by 4 but not 100
══════════════════════════════════════════════════

Enter a year to check: 2100

══════════════════════════════════════════════════
                LEAP YEAR CHECKER
══════════════════════════════════════════════════
Year   : 2100
Status : NOT A LEAP YEAR
Reason : Divisible by 4 and 100, but not 400
══════════════════════════════════════════════════

Enter a year to check: 2000

══════════════════════════════════════════════════
                LEAP YEAR CHECKER
══════════════════════════════════════════════════
Year   : 2000
Status : LEAP YEAR
Reason : Divisible by 4, 100, and 400
══════════════════════════════════════════════════

Enter a year to check: 2023

══════════════════════════════════════════════════
                LEAP YEAR CHECKER
══════════════════════════════════════════════════
Year   : 2023
Status : NOT A LEAP YEAR
Reason : Not divisible by 4
══════════════════════════════════════════════════

"""
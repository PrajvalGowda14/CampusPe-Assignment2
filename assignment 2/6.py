"""
Question 6: Grade Calculator
"""

# input marks for 5 subjects
sub1 = eval(input("Enter marks for Subject 1: "))
sub2 = eval(input("Enter marks for Subject 2: "))
sub3 = eval(input("Enter marks for Subject 3: "))
sub4 = eval(input("Enter marks for Subject 4: "))
sub5 = eval(input("Enter marks for Subject 5: "))

# calculate total
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
per = (total_marks / 500) * 100

# assign grade
if per >= 90:
    grade = "A+"
elif per >= 80:
    grade = "A"
elif per >= 70:
    grade = "B"
elif per >= 60:
    grade = "C"
elif per >= 50:
    grade = "D"
else:
    grade = "F"

# check for pass/fail
if min(sub1, sub2, sub3, sub4, sub5) >= 40:
    result = "PASS"
else:
    result = "FAIL"

width = 40
p_str = f"{per:.2f}%"

# printing report card
print("\n╔" + "═" * (width - 2) + "╗")
print(f"║{'REPORT CARD':^{width-2}}║")
print("╔" + "═" * (width - 2) + "╗")
print(f"║ Total Marks : {total_marks}/500" + " " * (width - 22 - len(str(total_marks))) + " ║")
print(f"║ Percentage  : {p_str}" + " " * (width - 18 - len(p_str)) + " ║")
print(f"║ Grade       : {grade}" + " " * (width - 18 - len(grade)) + " ║")
print(f"║ Result      : {result}" + " " * (width - 18 - len(result)) + " ║")
print("╚" + "═" * (width - 2) + "╝")



"""
OUTPUT:

Enter marks for Subject 1: 85
Enter marks for Subject 2: 92
Enter marks for Subject 3: 78
Enter marks for Subject 4: 88
Enter marks for Subject 5: 95

╔══════════════════════════════════════╗
║             REPORT CARD              ║
╔══════════════════════════════════════╗
║ Total Marks : 438/500                ║
║ Percentage  : 87.60%                 ║
║ Grade       : A                      ║
║ Result      : PASS                   ║
╚══════════════════════════════════════╝

"""
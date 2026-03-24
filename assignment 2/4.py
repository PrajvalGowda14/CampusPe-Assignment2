"""
Question 4: Age Calculator (Simple Bonus)
"""

from datetime import date

# current date
today = date.today()
curr_year = today.year
curr_month = today.month
curr_day = today.day

# input for birth date
b_day = int(input("Enter birth day (1-31): "))
b_month = int(input("Enter birth month (1-12): "))
b_year = int(input("Enter birth year: "))

age = curr_year - b_year            # age estimate

if (curr_month, curr_day) < (b_month, b_day):       # if the birthday hasnt come this year
    age = age - 1

# calculating age
months = age * 12
days = age * 365 
hours = days * 24
minutes = hours * 60
years_to_100 = 100 - age


# printing calculated age
print(f"\nResults for birth date {b_day}/{b_month}/{b_year}:")

print(f"Current age: {age} years")
print(f"Age in months: {months} months")
print(f"Age in days: {days} days")
print(f"Age in hours: {hours} hours")
print(f"Age in minutes: {minutes} minutes")
print(f"Years until age 100: {years_to_100} years")



"""
OUTPUT:

Enter birth day (1-31): 14
Enter birth month (1-12): 9
Enter birth year: 2004

Results for birth date 14/9/2004:
Current age: 21 years
Age in months: 252 months
Age in days: 7665 days
Age in hours: 183960 hours
Age in minutes: 11037600 minutes
Years until age 100: 79 years

"""
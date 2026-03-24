"""
Question 13: Sum and Average Calculator
"""

width = 30

# taking initial count
count = int(input("How many numbers? "))

# initializing list
numbers = []

# loop to take multiple inputs
for i in range(1, count + 1):
    val = eval(input(f"Enter number {i}: "))
    numbers.append(val)     # add numbers to the list

# calculating results
total_sum = sum(numbers)
average = total_sum / count
maximum = max(numbers)
minimum = min(numbers)

# print stats
print("\n" + "═" * width)
print(f"{'STATISTICS SUMMARY':^{width}}")
print("═" * width)
print(f"Sum      : {total_sum}")
print(f"Average  : {round(average, 2)}")
print(f"Maximum  : {maximum}")
print(f"Minimum  : {minimum}")
print("═" * width)



"""
OUTPUT:

How many numbers? 10
Enter number 1: 20
Enter number 2: 30
Enter number 3: 40
Enter number 4: 50
Enter number 5: 60
Enter number 6: 70
Enter number 7: 80
Enter number 8: 90
Enter number 9: 100
Enter number 10: 111

══════════════════════════════
      STATISTICS SUMMARY
══════════════════════════════
Sum      : 651
Average  : 65.1
Maximum  : 111
Minimum  : 20
══════════════════════════════

"""
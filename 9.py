"""
Question 9: Ticket Pricing System
"""

# input Age, Day of week, Number of tickets

age = eval(input("Enter age: "))
day = input("Enter day of week: ").lower()
num_tickets = eval(input("Number of tickets: "))

# calculate ticket price
if age < 3:
    price = 0
    cat = "Free (Infant)"
elif 3 <= age <= 12:
    price = 150
    cat = "Child"
elif 13 <= age <= 59:
    price = 300
    cat = "Adult"
else:
    price = 200
    cat = "Senior"

# check for discount
dis_perc = 0
weekend_days = ["friday", "saturday", "sunday"]

if day in weekend_days:
    dis_perc = 20

dis_amount = price * (dis_perc / 100)
final_price_per_ticket = price - dis_amount
total_amount = final_price_per_ticket * num_tickets

width = 50

# printing bill
print("\n" + "═" * width)
print(f"{'TICKET SUMMARY':^{width}}")
print("═" * width)
print(f"Category    : {cat}" + " " * (width - 18 - len(cat)))
print(f"Base Price  : ₹{price:.2f}")
print(f"Discount    : ₹{dis_amount:.2f} ({dis_perc}%)")
print(f"Final Price : ₹{final_price_per_ticket:.2f}")
print("═" * width)
print(f"Total ({num_tickets}) : ₹{total_amount:.2f}")
print("═" * width)



"""
OUTPUT:

Enter age: 25
Enter day of week: Friday
Number of tickets: 2

══════════════════════════════════════════════════
                  TICKET SUMMARY
══════════════════════════════════════════════════
Category    : Adult
Base Price  : ₹300.00
Discount    : ₹60.00 (20%)
Final Price : ₹240.00
══════════════════════════════════════════════════
Total (2) : ₹480.00
══════════════════════════════════════════════════

Enter age: 12
Enter day of week: Sunday
Number of tickets: 1

══════════════════════════════════════════════════
                  TICKET SUMMARY
══════════════════════════════════════════════════
Category    : Child
Base Price  : ₹150.00
Discount    : ₹30.00 (20%)
Final Price : ₹120.00
══════════════════════════════════════════════════
Total (1) : ₹120.00
══════════════════════════════════════════════════

Enter age: 2
Enter day of week: monday    
Number of tickets: 2

══════════════════════════════════════════════════
                  TICKET SUMMARY
══════════════════════════════════════════════════
Category    : Free (Infant)
Base Price  : ₹0.00
Discount    : ₹0.00 (0%)
Final Price : ₹0.00
══════════════════════════════════════════════════
Total (2) : ₹0.00
══════════════════════════════════════════════════

Enter age: 70
Enter day of week: Tuesday
Number of tickets: 2

══════════════════════════════════════════════════
                  TICKET SUMMARY
══════════════════════════════════════════════════
Category    : Senior
Base Price  : ₹200.00
Discount    : ₹0.00 (0%)
Final Price : ₹200.00
══════════════════════════════════════════════════
Total (2) : ₹400.00
══════════════════════════════════════════════════

"""
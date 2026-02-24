"""
Question 5: Bill Splitter
"""

# input for the bill details
total_bill = eval(input("Enter total bill: "))      # can have decimal vales
people = int(input("Number of people: "))           # cant have fraction of a person
tax_perc = eval(input("Tax percentage: "))          # can have decimal vales for the rest
tip_perc = eval(input("Tip percentage: "))

# calculation logic
tax_amount = total_bill * (tax_perc / 100)
bill_after_tax = total_bill + tax_amount
tip_amount = bill_after_tax * (tip_perc / 100)          # tip calculated on after tax amt
total_amt = bill_after_tax + tip_amount
per_person = total_amt / people

width = 50

# formatting strings
v1 = f"₹{total_bill:.2f}"
v2 = f"₹{tax_amount:.2f}"
v3 = f"₹{bill_after_tax:.2f}"
v4 = f"₹{tip_amount:.2f}"
v5 = f"₹{total_amt:.2f}"
v6 = f"₹{per_person:.2f}"

# printing bill breakdown
print("\n╔" + "═" * (width - 2) + "╗")
print(f"║{'BILL BREAKDOWN':^{width-2}}║")
print("╔" + "═" * (width - 2) + "╗")
print(f"║ Subtotal   : {v1}" + " " * (width - 17 - len(v1)) + " ║")                                     # 17 is the length of the labels like "║ Subtotal   :  ║"
print(f"║ Tax ({tax_perc}%)  : {v2}" + " " * (width - 15 - len(str(tax_perc)) - len(v2)) + " ║")        # 15 because tip and tax will be less than totals
print(f"║ After tax  : {v3}" + " " * (width - 17 - len(v3)) + " ║")
print(f"║ Tip ({tip_perc}%)  : {v4}" + " " * (width - 15 - len(str(tip_perc)) - len(v4)) + " ║")
print(f"║ Total      : {v5}" + " " * (width - 17 - len(v5)) + " ║")
print("╠" + "═" * (width - 2) + "╣")
print(f"║ Per person : {v6}" + " " * (width - 17 - len(v6)) + " ║")
print("╚" + "═" * (width - 2) + "╝")



"""
OUTPUT:

Enter total bill: 1000
Number of people: 4
Tax percentage: 10
Tip percentage: 15

╔════════════════════════════════════════════════╗
║                 BILL BREAKDOWN                 ║
╠════════════════════════════════════════════════╣
║ Subtotal   : ₹1000.00                          ║
║ Tax (10%)  : ₹100.00                           ║
║ After tax  : ₹1100.00                          ║
║ Tip (15%)  : ₹165.00                           ║
║ Total      : ₹1265.00                          ║
╠════════════════════════════════════════════════╣
║ Per person : ₹316.25                           ║
╚════════════════════════════════════════════════╝

"""
"""
Question 10: Simple ATM Simulator
"""

# initial values
balance = 10000
min_balance = 500
width = 30

# processing transactions in a loop
while True:

    # printing menu
    print("\n" + "═" * width)
    print(f"{'ATM SIMULATOR':^{width}}")
    print("═" * width)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("═" * width)

    choice = input("Enter choice: ")

    if choice == '4':
        print("Exiting...")
        break

    msg = ""           # transaction message
    status = ""        # success/failure status

    # calculating atm operations
    if choice == '1':
        status = "Success"
        msg = f"Balance: ₹{balance}"
    
    elif choice == '2':
        dep = eval(input("Enter amount to deposit: "))
        balance += dep
        status = "Success"
        msg = f"New Balance: ₹{balance}"
        
    elif choice == '3':
        wit = eval(input("Enter amount to withdraw: "))
        
        # rule check for minimum balance
        if (balance - wit) < min_balance:
            status = "Failed"
            msg = "Min balance ₹500 required"
        else:
            balance -= wit
            status = "Success"
            msg = f"New Balance: ₹{balance}"
            
    else:                                                           # incorrect choice
        print("Invalid choice! Please try again.")
        continue

    # print result of transaction
    print("\n" + "═" * width)
    print(f"Status: {status}")
    print(f"{msg}")
    print("═" * width)

"""
OUTPUT:

══════════════════════════════
        ATM SIMULATOR         
══════════════════════════════
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
══════════════════════════════
Enter choice: 3
Enter amount to withdraw: 2000

══════════════════════════════
Status: Success
New Balance: ₹8000
══════════════════════════════

MENU

Enter choice: 3
Enter amount to withdraw: 7800

══════════════════════════════
Status: Failed
Min balance ₹500 required
══════════════════════════════

MENU

Enter choice: 1

══════════════════════════════
Status: Success
Balance: ₹8000
══════════════════════════════

MENU

Enter choice: 4
Exiting...
"""
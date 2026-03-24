"""
Question 11: Number Pattern Printer
"""

width = 30

# processing patterns in a loop
while True:

    # printing menu
    print("\n" + "═" * width)
    print(f"{'NUMBER PATTERN MENU':^{width}}")
    print("═" * width)
    print("""1. Pattern 1 
            1
            1 2
            1 2 3
            1 2 3 4
            1 2 3 4 5""")
    print("""2. Pattern 2 
            1
            2 2
            3 3 3
            4 4 4 4
            5 5 5 5 5""")
    print("""3. Pattern 3
            5 4 3 2 1
            4 3 2 1
            3 2 1
            2 1
            1""")
    print("""4. Pattern 4
            1
           121
          12321
         1234321
        123454321""")
    print("5. Exit")
    print("═" * width)

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting...")
        break
    
    # checking for valid choice before asking for height
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please try again.")
        continue

    h = eval(input("Enter height of pattern: "))
    print("\n" + "═" * width)

    # pattern generation logic
    if choice == '1':                       # increment i after each row and print i numbers
        for i in range(1, h + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif choice == '2':                     # increment i after each row and print val of i for i number of times
        for i in range(1, h + 1):
            print(f"{i} " * i)

    elif choice == '3':                     # start from height val and print decrement and decrease the height after each row
        for i in range(h, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    elif choice == '4':
        for i in range(1, h + 1):            
            print(" " * (h - i), end="")    # print spaces
            for j in range(1, i + 1):       # Print increasing numbers
                print(j, end="")            
            for j in range(i - 1, 0, -1):   # Print decreasing numbers
                print(j, end="")            
            print()

    print("═" * width)

"""
OUTPUT:

══════════════════════════════
     NUMBER PATTERN MENU      
══════════════════════════════
1. Pattern 1 (1, 12, 123...)
2. Pattern 2 (1, 22, 333...)
3. Pattern 3 (54321, 4321...)
4. Pattern 4 (1, 121, 12321...)
5. Exit
══════════════════════════════
Enter your choice (1-5): 4
Enter height of pattern: 5

══════════════════════════════
1
121
12321
1234321
123454321
══════════════════════════════

MENU

Enter your choice (1-5): 4
Enter height of pattern: 7

══════════════════════════════
      1
     121
    12321
   1234321
  123454321
 12345654321
1234567654321
══════════════════════════════

MENU

Enter your choice (1-5): 3
Enter height of pattern: 9

══════════════════════════════
9 8 7 6 5 4 3 2 1
8 7 6 5 4 3 2 1
7 6 5 4 3 2 1
6 5 4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
══════════════════════════════

MENU

Enter your choice (1-5): 2
Enter height of pattern: 4

══════════════════════════════
1
2 2
3 3 3
4 4 4 4
══════════════════════════════

MENU

Enter your choice (1-5): 5
Exiting...
"""
"""
Question 12: Multiplication Table Generator
"""

width = 50

# printing heading
print("\n" + "═" * width)
print(f"{'MULTIPLICATION PROGRAM':^{width}}")
print("═" * width)

# input number and range
num = eval(input("Enter number: "))
r = eval(input("Enter range (end): "))

print("\n" + "═" * width)
print(f"{f'Multiplication Table of {num}':^{width}}")
print("═" * width)

# loop for printing single table
for i in range(1, r + 1):
    print(f"{f'{num} x {i} = {num * i}':^{width}}")

print("\n" + "═" * width)
print(f"{'FULL MULTIPLICATION GRID (1-10)':^{width}}")
print("═" * width)

for i in range(1, 11):
    for j in range(1, 11):
        # used f-string with :4 for perfect column alignment
        print(f"{i * j:4}", end=" ")
    print()
print("═" * width)



"""
OUTPUT:

══════════════════════════════════════════════════
              MULTIPLICATION PROGRAM
══════════════════════════════════════════════════
Enter number: 7
Enter range (end): 12

══════════════════════════════════════════════════
            Multiplication Table of 7
══════════════════════════════════════════════════
                    7 x 1 = 7
                    7 x 2 = 14
                    7 x 3 = 21
                    7 x 4 = 28
                    7 x 5 = 35
                    7 x 6 = 42
                    7 x 7 = 49
                    7 x 8 = 56
                    7 x 9 = 63
                   7 x 10 = 70
                   7 x 11 = 77
                   7 x 12 = 84

══════════════════════════════════════════════════
         FULL MULTIPLICATION GRID (1-10)
══════════════════════════════════════════════════
   1    2    3    4    5    6    7    8    9   10
   2    4    6    8   10   12   14   16   18   20
   3    6    9   12   15   18   21   24   27   30
   4    8   12   16   20   24   28   32   36   40
   5   10   15   20   25   30   35   40   45   50
   6   12   18   24   30   36   42   48   54   60
   7   14   21   28   35   42   49   56   63   70
   8   16   24   32   40   48   56   64   72   80
   9   18   27   36   45   54   63   72   81   90
  10   20   30   40   50   60   70   80   90  100
══════════════════════════════════════════════════

"""
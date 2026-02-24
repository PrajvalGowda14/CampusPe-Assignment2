"""
Question 16: Number Guessing Game
"""

import random

width = 30
best_score = 8  # Initializing with a value higher than max attempts

# main game loop to allow playing again
while True:
    print("\n" + "═" * width)
    print(f"{'NUMBER GUESSING GAME':^{width}}")
    print("═" * width)
    
    target = random.randint(1, 100)
    attempts_left = 7
    won = False

    # guessing loop
    while attempts_left > 0:
        print(f"\nAttempts remaining: {attempts_left}")
        guess = int(input("Guess a number (1-100): "))
        
        # logical checks for the guess
        if guess == target:                             # correctly guessed
            attempts_used = 8 - attempts_left
            print("\n" + "═" * width)
            print("CONGRATULATIONS!!")
            print(f"You guessed it in {attempts_used} attempts")    # num of attempts
            
            if attempts_used < best_score:              # high score
                best_score = attempts_used
                print("NEW BEST SCORE!")
            
            print("═" * width)
            won = True
            break
            
        elif guess < target:                            # build message string
            msg = "Too Low!"
        else:
            msg = "Too High!"

        if abs(guess - target) <= 5:                    # add too close to the string
            msg += " (You're very close!)"
            
        print(msg)
        attempts_left -= 1

    if not won:                                         # failed
        print("\n" + "═" * width)
        print("GAME OVER")
        print(f"The number was: {target}")              # reveal number
        print("═" * width)

    # display best score so far
    if best_score <= 7:
        print(f"Current Best Score: {best_score} attempts")

    # play again check
    choice = input("\nPlay again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing! Goodbye.")
        break



"""
OUTPUT:

══════════════════════════════
     NUMBER GUESSING GAME
══════════════════════════════

Attempts remaining: 7
Guess a number (1-100): 50
Too Low!

Attempts remaining: 6
Guess a number (1-100): 75
Too High!

Attempts remaining: 5
Guess a number (1-100): 62

══════════════════════════════
CONGRATULATIONS!
You guessed it in 3 attempts
NEW BEST SCORE!
══════════════════════════════
Current Best Score: 3 attempts

Play again? (y/n): N
Thanks for playing! Goodbye.

"""


"""
OUTPUT 2:


══════════════════════════════
     NUMBER GUESSING GAME
══════════════════════════════

Attempts remaining: 7
Guess a number (1-100): 50
Too High!

Attempts remaining: 6
Guess a number (1-100): 20
Too Low!

Attempts remaining: 5
Guess a number (1-100): 30
Too High! (You're very close!)

Attempts remaining: 4
Guess a number (1-100): 35
Too High!

Attempts remaining: 3
Guess a number (1-100): 25
Too Low! (You're very close!)

Attempts remaining: 2
Guess a number (1-100): 27

══════════════════════════════
CONGRATULATIONS!
You guessed it in 6 attempts
NEW BEST SCORE!
══════════════════════════════
Current Best Score: 6 attempts

Play again? (y/n): N
Thanks for playing! Goodbye.

"""
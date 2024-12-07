import random

# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

# Let's play a guessing game to practice what we've learned
print(CYAN + " ------------------------------------" + RESET)
print(CYAN + "|    Welcome to Guess Game Play 🎮   |" + RESET)
print(CYAN + " ------------------------------------" + RESET)
print(YELLOW + " -----> Please Guess a number <------" + RESET)

# Generate a random number
min_size = 1
max_size = 100  # Limiting the range for a practical game
random_number = random.randint(min_size, max_size)

# Allow the user 3 attempts to guess the number
attempts = 3

while attempts > 0:
    print(BLUE + f"\nYou have {attempts} attempt(s) left." + RESET)
    guess = input(MAGENTA + "Guess a number: " + RESET)

    # Check if the input is a valid digit
    if not guess.isdigit():
        print(RED + "Please enter a valid number!" + RESET)
        continue  # Skip to the next iteration
    
    # Convert the guess to an integer
    guess = int(guess)
    
    # Check the user's guess
    if guess == random_number:
        print(GREEN + "🥳 OWWW WHAT A LEGEND YOU ARE 🔥🎇" + RESET)
        break
    else:
        print(RED + "Oops! Wrong guess. Try again.\n" + RESET)
    
    # Decrement the number of attempts
    attempts -= 1

# If the user runs out of attempts
if attempts == 0:
    print(RED + "Oooh Please don't cry 🥺" + RESET)
    print(YELLOW + f"The correct number was {random_number}. Good luck next time! 🤡" + RESET)

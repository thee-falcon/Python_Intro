import random
import sys

# Let's play a guessing game to practice what we've learned

print(" ------------------------------------")
print("|    Welcome to Guess Game Play 🎮   |")
print(" ------------------------------------")
print(" -----> Please Guess a number <------")

# Generate a random number
min_size = 1
max_size = 100  # Limiting the range for a practical game
random_number = random.randint(min_size, max_size)

# Allow the user 3 attempts to guess the number
attempts = 3

while attempts > 0:
    guess = input(f"You have {attempts} attempt(s) left. Guess a number: ")

    # Check if the input is a valid digit
    if not guess.isdigit():
        print("\033[31mPlease enter a valid number!\033[0m")
        continue  # Skip to the next iteration
    
    # Convert the guess to an integer
    guess = int(guess)
    
    # Check the user's guess
    if guess == random_number:
        print("🥳 OWWW WHAT A LEGEND YOU ARE 🔥🎇")
        break
    else:
        print("Oops! Wrong guess. Try again.\n")
    
    # Decrement the number of attempts
    attempts -= 1

# If the user runs out of attempts
if attempts == 0:
    print("Oooh Please don't cry 🥺")
    print(f"The correct number was {random_number}. Good luck next time! 🤡")


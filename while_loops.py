import random
import sys

# let's play a guessing game just to improve what we learn

print(" ------------------------------------")
print("|    Welcome to Guess Game Play 🎮   |")
print(" ------------------------------------")
print(" -----> Please Guess a number <------")

# store the data from user
guess = input("The number: ")

# check the data is an integer or is a string, actualy the input it's returns a string but we can check it if if the input is a number or something else
if guess.isdigit():
    max_size = sys.maxsize
    min_size = -sys.maxsize - 1
    #  if you want to Win in this game you should be a legend hahahahahahahahahahahahahahaha 😈
    ranndom = random.randint(min_size, max_size)
    counter = 0
    many_try = 0
    while counter <= 2:
        if guess == ranndom:
            print("🥳 OWWW WHAT A LEGEND YOU ARE 🔥🎇")
        else:
            print("Ochhhii Are you lost baby??😍\n")
            guess_two = input("Try again 😘: ")
            if guess_two == ranndom:
                print("🥳 OWWW WHAT A LEGEND YOU ARE 🔥🎇")
            many_try += 1
            counter += 1
        print("====> " + str(counter))
        if many_try > 2:
            print("Oooh Please don't CRY 🥺")
            print("Good luck next TIME HAHAHAH 🤡")
            break
else:
    print("\033[31mPlease Enter a Digit\033[0m")
    
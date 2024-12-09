import time
import os

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

manual = '''
                Help Manual Commands📖

❶ start: To Start the game.
❷ stop: To Stop the game.
❸ quit: To Quit the game.
❹ help: To Manual Commands.

                    Enjoy 🎮
'''

print(CYAN + " ------------------------------------" + RESET)
print(CYAN + "|    Welcome to Car Game Play 🚗     |" + RESET)
print(CYAN + " ------------------------------------\n" + RESET)
print(manual)
print( MAGENTA + "Please Enter the command: " + RESET)

# array of commands
commands = ["start", "stop", "quit"]

# let's define a function that clear the console(Screen)
# yeah I'm still new in Python but I'm already know the concept and the syntax is easy
def clear_console():
    # cls if the operating system is windiws otherwise clear for ios
    os.system('cls' if os.name == 'nt' else 'clear')

# simulate car movement
def car_animation():
    frames = ["🚗💨     ", " 🚗💨   ", "   🚗💨 ", "    🚗💨     ", "      🚗💨   ", "       🚗💨 ", "        🚗💨", "         🚗💨   ", "           🚗💨 ", "            🚗💨", "              🚗💨  ", "                  🚗💨 "]
    while car_moving:
            for frame in frames:
                print(frame, end="\r", flush=True)
                time.sleep(0.3)
# game state 
car_moving = False

while True:
    command = input(">> ")

    cmnd = command.strip().lower()
    if (cmnd == "quit"):
        print(GREEN + "Proccess finished with exit code 0" + RESET)
        break

    if cmnd not in commands:
        print(RED + "Uknown Command Please enter 'start', 'stop' or 'quit', You can see Help Manual 'help'." + RESET)
        continue
    if (cmnd == "start"):
        if car_moving:
            print(BLUE + "The car is already is moving..." + RESET)
        else:
            print("Car Started... 🚗💨")
            car_moving = True
            clear_console()
            car_animation()
    elif cmnd == "stop":
        if not car_moving:
            print(YELLOW + "The car is already stopped!" + RESET)
        else:
            print(CYAN + "Car stopped!" + RESET)
            car_moving = False

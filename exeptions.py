RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

# to handle Erros in Python Program we use try except
try:
    age =  int(input("Please enter your Age: ")) # this line of code should give us an error compiling when we try to input a string insted integer
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print(YELLOW + "Please the Age cannot be 0." + RESET)
except ValueError:
    print(YELLOW + "INVALID VALUE, Please Enter a Digit" + RESET)

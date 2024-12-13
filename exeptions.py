RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

# to handle Erros in Python Program we use try except
try:
    file = open("app.py") # we open a file names app.py
    age =  int(input("Please enter your Age: ")) # this line of code should give us an error compiling when we try to input a string insted integer
    income = 20000
    risk = income / age
    print(age)
except (ZeroDivisionError, ValueError) as ERROR:
    print(YELLOW + "INVALID VALUE, Please Enter a Digit greater then 0" + RESET)
    print(RED + str(ERROR) + RESET)
    print(CYAN + str(type(ERROR)) +RESET)
except KeyboardInterrupt:
    print(MAGENTA + "\nThe Program is " + GREEN + "Exit " + RESET + MAGENTA + "Successfully." + RESET)
else:
    print(GREEN + "No exeption were thrown" + RESET)
finally: # a finally kwyword block will be executed no matter if the try block raises an error or not
         # This can be useful to close objects and clean up resources
    
    file.close() # we close the app.py file, because when a file is open, the operating system allocates memory and other
                 # resources to the file, which can potentialy impact the performance of the system if too many files are
                 # opend at the same time

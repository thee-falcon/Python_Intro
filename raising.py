RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default


# The 'raise' keyword is used to raise an exception. You can define what kind of error to raise, and text to print to the user

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError(RED + "Age Cannot be Zero(0) or less than 0." + RESET)
    return 10 / age


try:
    print(calculate_xfactor(0))
except ValueError as error:
    print(error)

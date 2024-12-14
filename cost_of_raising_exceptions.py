RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

from timeit import timeit

code1 = """

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError(RED + "Age Cannot be Zero(0) or less than 0." + RESET)
    return 10 / age


try:
    print(calculate_xfactor(0))
except ValueError as error:
    print(error)
"""

code_2 = """
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

calc_x = calculate_xfactor(0)
if calc_x == None:
    pass

"""

time1 = timeit(code1, number=10000)
time2 = timeit(code_2, number=10000) # code2 is better if we work for a performance program, because we don't use "exceptions", we use 'pass' to avoid getting an error when code is not allowed

print(YELLOW + "first code=", time1)
print("second code=", time2)
print(RESET + BLUE + f"==>> Difference between time1 and time2= {time1 - time2}" + RESET)

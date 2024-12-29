# the sys module in python provides various functions and variables that are used to manipulate different parts of the Python runtime environement.
# It allows operating in the interpreter as it provides access to the variables and functions that interact strongly with the intrepreter.
import sys

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password: " + password)

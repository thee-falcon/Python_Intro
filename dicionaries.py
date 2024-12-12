RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

# dictionaries are used to store data values in => key:value pairs
# each key should be unique in dictionary

customer = {
    "name": "Thee-falcon",
    "age": 25,
    "is_verified": True
}

# print(customer["name"]) => it's not good practice
# we have a method names get(), this method returns the value of the key, if the key is dos'nt exist in dictionary returns None
# so this method is safe rather than customer["NAME"], it will give us an error in compiling time

print(customer.get("NAME")) # should print None, because we don't have NAME in dictionary keys

print(customer.get("birthdate", "JUN 29")) # this line of code, should work, yeah we don't have birthdate in our dictionary
                                           # but the method get() will add the 'birthdate' key with 'JUN 29' value into dictionary
                                           # because we give it a value => JUN 29


# let's solve a problem:
# a program that asks our phone number, we type it in digit and then sould translate it to words.
# for Example:
# Phone: 123
# Output:
# One Two Three

# let's declare a dictionary of the names of numbers
numbers = {
    '0': "Zero",'1': "One", '2': "Two", '3': "Three",
    '4': "Four", '5': "Five", '6': "Six", '7': "Seven",
    '8': "Eight", '9': "Nine"}

phone_from_user = input("Please Enter you phone number: ").strip()
# check if the input is not numeric
if not phone_from_user.isdigit():
    print(RED + "\n🚫 Please Enter Digits ONLY!!!" + RESET)
    exit()

print(MAGENTA + "\nConverting from Digits to Words..." + RESET)

# convert each digit to its corresponding word
output = []
for digit in phone_from_user:
    output.append(numbers.get(digit))

# join the words with spaces and print the result
print(YELLOW + "✅ " + " ".join(output) + RESET)
print(GREEN + "             Done 😘" + RESET)



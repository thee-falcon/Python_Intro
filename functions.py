# A function is a block of code which only runs when it us called. You can pass data, known as parameters, into a function.

def display_message_to_user(firs_name, last_name):
    print(f"Hi dear user: {firs_name} {last_name} <3")

def square(number):
    print(number * number)

print("Start")
display_message_to_user("Omar", last_name="Makran")
print("Finish!")

print(square(3)) # should print 9 and None because we don't add the return of the function, so python by default return None (NULL)
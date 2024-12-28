# learn how to generate random values in python
import random
import string


print(random.random()) # print a random float number
print(random.randint(1, 10)) # print a random int from 'a' to 'b'
print(random.choice([1, 2, 4, 5, 2])) # print a choice from the list
print(random.choices(["apple", "banana", "cherry"], [10, 1, 1], k= 14))

# if we want to generat a random password, we can work with string module
password = ""
print(password.join(random.choices(string.ascii_letters + string.digits, k=12)))

# if we want to shuffle a list, we can use the method shuffle from random
list = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(list)
print(list)
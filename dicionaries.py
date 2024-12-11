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


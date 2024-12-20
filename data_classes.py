# namedtuple: It provides a way to create simple, lightweight data structers similar to class, but without the overhead of defining fa full class
# like a dicitionaries, the contain keys that are hashed to a particular value.
# On the contrary, it supports both access from key-value and itraration, the functionality that dictionary lack.

# Python NamedTuple Syntax:
# namedtuple(typenamem field_names)
# typename: The name of the namedtuple
# field_names: The list of attributes stored in the namedtuple

from collections import namedtuple

# create a class that is like a lightweight version of class, but immutable properties(like tuples)
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
# compare the values of all fields between two instance, not their identities(memory addres)
# p1.__eq__(p2)
# since both p1 and p2 are instances of the same Point class, python compares their fields(x and y)
# p1.x == p2.x => True (1 == 1)
# p1.y == p2.y => True (2 == 2)
print(p1 == p2) # will print True

print(p1 is p2) # will print False becasue p1 and p2 are different objects stored at different memory locations.
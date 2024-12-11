numbers = [3, 4, 6, 1, 75, 2, 1, 3]

# this method append the number 10 in end of the list
numbers.append(10)
print("append(10)")
print(numbers)

# we use insert to add a item to specific index
numbers.insert(4, 10)
print("insert(4, 10)")
print(numbers)

# to remove the last item in the list
numbers.pop()
print("pop()")
print(numbers)

# return the numbers of duplicate to specific item in the list
print(numbers.count(1))

# if we want to sort a list, we should use sort
print("sort the list")
numbers.sort()
print(numbers)
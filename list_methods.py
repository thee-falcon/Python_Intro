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


# Problem solving time, let's solve a simple Problem:
# Write a program to remove the duplicate in a list

print("=============Problem Solving:==============\n")
nums = [2, 2, 4, 6 , 3, 4, 6, 1]
#       0  1  2  3  4  5  6  7  8  9  10 11 12

nb = []

for nm in nums:
    dupli = nb.count(nm)
    # if nm not in nb => this is nother method to solve this problem
    if dupli < 1:
        nb.append(nm)

print(nb)
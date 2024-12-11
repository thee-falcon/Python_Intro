# simple problem solving to improv the list concept
# let's find the largest number into a list

numbers = [9, 3, 5, 54, 1000, 33, 22, 234, 38]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    
print(max_num) # should print the greatest number in the list
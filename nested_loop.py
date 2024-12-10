# nested loop is a loop inside a loop

# in function range, the number 4 is not included, so the while loop will stop in number 3
# for x in range(4):
#     for y in range(3):
#         print(f"(x:{x}, y:{y})")


# Let's solve this problem:

#  Output:
# XXXXX
# XX
# XXXXX
# XX
# XX


# Should Solve it using nested loop, yeah we can solve it using one for loop
# but should solve it using nested loops

# The solution
numbers = [5, 2, 5, 2, 2]

for i in numbers:
    output = ''
    for y in range(i):
        output += 'X'
    print(output)
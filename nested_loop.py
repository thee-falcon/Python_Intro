# nested loop is a loop inside a loop

# in function range, the number 4 is not included, so the while loop will stop in number 3
for x in range(4):
    for y in range(3):
        print(f"(x:{x}, y:{y})")

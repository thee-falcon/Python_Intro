RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Resets color to default

#=======>>>  A Class is like an object constructor, or, a "Blue Print" for creating an Object


# we declare a class names Point
class Point:

    default_color = "red"
    # we declare a constructor
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def draw(self):
        print(f"Draw => Point ({self.x}, {self.y})")

# We access to the Class Directly and change the value of 'default color', so all Attributes well get the same default color that we change
Point.default_color = "yellow"

# point is an object      
point = Point(1, 2)
# print the type of the point
print(type(point))
# will print the boolan of isinstance method to check if point is an instance of the Point Class
print(isinstance(point, Point))
print(YELLOW + point.default_color + RESET)
point.draw()

another = Point(3, 4)
print(YELLOW + another.default_color + RESET)
another.draw()
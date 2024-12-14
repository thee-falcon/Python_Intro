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
    def draw(self):
        print("draw")

# point is an object      
point = Point()
# print the type of the point
print(type(point))
# will print the boolan of isinstance method to check if point is an instance of the Point Class
print(isinstance(point, int))
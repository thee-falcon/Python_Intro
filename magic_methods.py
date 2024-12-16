
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x, self.y})"

    def draw(self):
        print(f"Point ({self.x, self.y})")


point = Point(1, 2)

point.draw() # will print: Point (1, 2)

print(point) # will print the return of magic __str__
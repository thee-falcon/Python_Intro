class Point:
    def __init__(self,x , y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, object) -> bool:
        return self.x == object.x and self.y == object.y
    
    def __gt__(self, object) -> bool:
        return self.x > object.x and self.y > object.y

point = Point(4, 24)
other = Point(1, 2)

print(point == other)
print(point > other)
# parent, base Class
# actually animal is not the base class in this program, because there is a bass class names: 'object'
class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("eat")

# child, subclass
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

fish = Fish()
fish.eat()
print(fish.age)

# here we will test if object is the base class in this program

print(isinstance(fish, object)) # will print: True
print(issubclass(Mammal, object)) # will print also: True
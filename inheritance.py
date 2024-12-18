# parent, base Class
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
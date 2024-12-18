# parent, base Class
class Animal:
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
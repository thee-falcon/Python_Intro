# method overriding is an ability of any object-oriented programming language that allows a subclass to provide a specific implementation
# of a method that is already provided by one of its super-classes or parent classes.

class Animal:
    # base constructor
    def __init__(self) -> None:
        self.age = 1
    
    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")


class Mammal(Animal):
    def __init__(self) -> None:
        self.height = 10
        super().__init__() # call parent constructor (Animal)

    def walk(self):
        print("walk")


class   Fish(Animal):


    def swim(self):
        print("swim")
    

mammal = Mammal()
print(mammal.age)
print(mammal.height)
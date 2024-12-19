# multilevel inheritance is a type of inheritance in which a class inherits from a class, which itself inhrits from another class.
# it allow a class to inherut properties and methods from multiple parents classes, froming a hierarchy similar to a family tree.

class   Flyer:
    def flay(self):
        print("Flay")

class   Swimmer:
    def swim(self):
        print("Swimmer")


class   FlyerFish(Flyer, Swimmer):
    def __init__(self) -> None:
        super().__init__()

    def flyer_chicken():
        print("FlyerChicken")

flayer_chick = FlyerFish()
flayer_chick.flay()
flayer_chick.swim()
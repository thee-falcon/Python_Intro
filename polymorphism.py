from abc import ABC, abstractmethod

class   UIControl(ABC):
    @abstractmethod
    def draw(self):
        # no implementation, we implement it in the subclasses
        pass


class   TextBox(UIControl):
    # we implement the draw method from UIControl ABSTRACT CLASS
    def draw(self):
        print("TextBox")


class   DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# this method take in argument ANY, it means take any data type, in our example we will use classes
def draw(controls):
    for control in controls:
        # will print the draw method of each class, TextBox and DropDownList
        control.draw()

ddl = DropDownList()
textbox = TextBox()

# we use an array to store our classes to it, and then itear for each class, to draw.
# that what we call Polymorphism. Poly means Many, morph means Forms
draw([ddl, textbox])

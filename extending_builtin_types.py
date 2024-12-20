# this change allow one to customize or extand the behavior of built-in types with userdefind class statements:
# simply subclass the new type names to customize them. Instances of your type subclasses can generally be used anywhere that the original builtin type can appear.

class Text(str):
    def duplicate(self):
        return self + self
    

class TrackableList(list):
    def append(self, object) -> None:
        print("Append called")


list = TrackableList()
list.append("12")

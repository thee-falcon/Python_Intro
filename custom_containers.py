class   TagCloud:
    def __init__(self) -> None:
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1 # 1 here is a counter of the Value
    
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    
    # tag is the key and count is the value
    def __setitem__(self, tag, count):
        # we should not return because the magic method returns None, it's a set just a value to the key
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)
    
    # to iterate to the dict
    # def __iter__(self):
    #     return iter(self.tags)
    

# will call the __init__ constructor
cloud = TagCloud()

# then will call the add() method
cloud.add("Python")
cloud.add("PyThon")
cloud.add("PyThon")
cloud.add("PyThon")
cloud.add("PyThon")
cloud.add("PyThone")
cloud.add("PyThonewr")

# to knowing the value of the key, we should declare a magic method names __getitem__
print(cloud["python"])

# to change the value of a key, we should declare the __setitem__ magic method
cloud["python"] = 0 # we update the value from 5 to 0

print(cloud.tags) # print the dictionary

# to represents the length of the object for which it is called. 
print(len(cloud))

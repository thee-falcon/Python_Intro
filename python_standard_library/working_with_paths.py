# we will learn how we can work with files and directories in python

from pathlib import Path

path = Path("ecommerce/__init__.py")
print(path.exists()) # this will print False because it doesn't exist
print(path.name) # this will print the name of file with extension: __init__.py
print(path.stem) # this will print __init__ without extension type: .py
print(path.suffix) # this will print the directory of the __init__ file
print(path.parent) # this will print the parent of the file

path = path.with_suffix(".txt") # just we present the path, we did not change the file extension name.
print(path)
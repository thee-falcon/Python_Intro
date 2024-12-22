from pathlib import Path
from time import ctime
import shutil

# path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt") # rename the name of the file
# path.unlink() # to delete it

# path.stat() return data of the file
# for example:
# if we need to print the date of the creation file we use ctime class to print date from it
# print(ctime(path.stat().st_ctime)) # will print: Sun Dec 22 01:25:29 20
# # we can read also bytes of the file
# print(path.read_bytes())
# # we can also read the content of the text
# print(path.read_text())

# to copy file to another file
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

shutil.copy(source, target)

from pathlib import Path

path = Path("ecommerce")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# ===>> [<expression> for <variable> in <iterable>]: List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# p: is a variable name, and this what gets added to the list for each iteration
# p.is_dir(): to filtering if is True, p is included in the resulting list Otherwise False is skipped.
paths = [p for p in path.iterdir() if p.is_dir()]  # will print: [PosixPath('ecommerce/sales'), PosixPath('ecommerce/shopping')]
# path.glob("*.py"): searches for all files in the ecommerce directory that match the pattern *.py
# this returns an iterator of Path objects representing all .py files.
py_files = [p for p in path.glob("*.py")]
print(py_files)
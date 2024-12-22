from pathlib import Path
from zipfile import ZipFile

# when we execute the program we will see a zipe file 
with ZipFile("files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)

# if we want read the data of the zip files
with ZipFile("files.zip") as zip:
    print(zip.namelist())
from pathlib import Path
from zipfile import ZipFile

# when we execute the program we will see a zipe file 
with ZipFile("files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)

# if we want read the data of the zip files
with ZipFile("files.zip") as zip:
    print(zip.namelist())
    # if we want to get information about specify file in zip file
    info = zip.getinfo("ecommerce/__init__.py")
    print(info) # this will print all information about the file
    # if we want a specifec information
    print(info.file_size)
    print(info.compress_size)
    print(info.date_time)
    # to extract all the files from the zip file
    zip.extractall("extract")
# JSON stands for JavaScript Object Notation and is a popular way to format data in a human readable
import json
from pathlib import Path

movies = [
    {"id": 1, "title": "The Terminator", "year": 1984},
    {"id": 2, "title": "Taken", "year": 2008}
]

# function will convert a subset of Python objects into a json string
data = json.dumps(movies)
print(data)
# if we want to write data in a json file
Path("movies.json").write_text(data)

# now we will read data from the JSON file.
data_read = Path("movies.json").read_text()
moviess = json.loads(data)
print(moviess) # print all the list of the movies
print(moviess[0]) # print the first dictionary in list
print(moviess[0]["title"]) # print the title of the movie
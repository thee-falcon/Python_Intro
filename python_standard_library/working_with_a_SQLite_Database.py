# SQLite is a lightweight database that we use for storing data on application

import sqlite3
import json
from pathlib import Path

# we load the data from movie json to movies variable
movies = json.loads(Path("movies.json").read_text())

# we gonna creat a file for data base
with sqlite3.connect("db.sqlite3") as con:
    # ?: id and title and year
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        con.execute(command, tuple(movie.values()))
    # now will be writen in data base
    con.commit()
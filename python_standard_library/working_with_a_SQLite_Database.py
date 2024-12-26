# SQLite is a lightweight database that we use for storing data on application

import sqlite3
import json
from pathlib import Path

# we load the data from movie json to movies variable
# movies = json.loads(Path("movies.json").read_text()) # this is commented because now we are done with json file
# now we will read data from database

# we gonna creat a file for database
with sqlite3.connect("db.sqlite3") as conn:
    # ?: id and title and year
    # command = "INSERT INTO Movies VALUES(?, ?, ?)" 
    # to read data from database we need to change the command
    command = "SELECT * FROM Movies"
    # and we don't need to iterat in movies, because now we need to read data from database
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
    
    # when we read data from database, we'll get a cursor
    cursor = conn.execute(command)
    # so we can iterate over it and get one row at a time
    for row in cursor:
        print(row) # we will get a tuple of values for a row in our database
    
    # we initialize it again, because the cursor is in the end of the file, so we should reset it to the beginning   
    cursor = conn.execute(command)
    # and we can return all rows in this table using this method
    list = cursor.fetchall()
    print(list)
    
    # now will be writen in database
    # conn.commit() # we don't need connection commit because we only need this when writing data for database
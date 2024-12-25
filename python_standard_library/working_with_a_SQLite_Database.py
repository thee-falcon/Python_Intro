# SQLite is a lightweight database that we use for storing data on application

import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())

print(movies)
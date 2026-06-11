import sqlite3


connection = sqlite3.connect('../../movies.db')

cursor = connection.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS movies (
    id INTEGER	PRIMARY KEY,
    title TEXT UNIQUE NOT NULL,
    director TEXT NOT NULL,
    year INTEGER NOT NULL,
    length_minutes INTEGER NOT NULL
    )
    """
)


cursor.execute("DELETE FROM movies")
cursor.execute("INSERT INTO movies (id, title, director, year, length_minutes) VALUES (3, 'Toy Story 3', 'John Lasseter', 2010, 81)")

movies = [
    (5, "Finding Nemo", "Andrew Stanton", 2003, 107),
    (6, "The Incredibles", "Brad Bird", 2004, 116),
    (7, "Cars", "John Lasseter", 2006, 117),
    (8, "Ratatouille", "Brad Bird", 2007, 115),
    (9, "WALL-E", "Andrew Stanton", 2008, 104),
    (10, "Up", "Pete Docter", 2009, 101),
    (12, "Cars 2", "John Lasseter", 2011, 120),
    (13, "Brave", "Brenda Chapman", 2012, 102),
    (14, "Monsters University", "Dan Scanlon", 2013, 110),
    (87, "WALL-G", "Brenda Chapman", 2042, 97),
]
cursor.executemany("INSERT INTO movies (id, title, director, year, length_minutes) VALUES (?, ?, ?, ?, ?)", movies)

cursor.execute("SELECT * FROM movies")
data = cursor.fetchall()


for i in data:
    _id, title, director, year, length_minutes = i
    print(_id, title, director, year, length_minutes)

cursor.execute(
    """
    UPDATE movies
    SET title = ?, director = ?, year = ?, length_minutes = ?
    WHERE id = ?
    """,
    ("WALL-E 2", "Brenda Chapman", 2042, 97, 87)
)

cursor.execute(
    """
    DELETE FROM movies
    WHERE id = ?
    """,
    (12,)
)

connection.commit()

connection.close()

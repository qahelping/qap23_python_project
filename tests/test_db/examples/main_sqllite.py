import sqlite3

connection = sqlite3.connect('memes.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS memes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
    )
""")

connection.commit()

cursor.execute("INSERT INTO memes (name) VALUES (?)", ("Токсис",))
cursor.execute("INSERT INTO memes (name) VALUES (?)", ("Kot в сапогах",))
connection.commit()

cursor.execute("SELECT * from memes")
data = cursor.fetchall()

for row in data:
    print(row)


cursor.execute("""
SELECT * FROM memes
WHERE memes.name = 'Kot в сапогах'
"""
               )
data = cursor.fetchall()

for row in data:
    print(row)


cursor.close()
connection.close()

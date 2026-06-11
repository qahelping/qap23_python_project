import os

from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///test.db", echo=True)

with engine.connect() as connection:
    connection.execute(text("DROP TABLE IF EXISTS users"))

    connection.execute(text("""
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    is_active BOOLEAN
    )
    """))

    connection.execute(text("INSERT INTO users (name, email, is_active) VALUES ('Anna', 'anna_email@gmail.com', 1)"))

    # connection.commit()
    #
    # connection.execute(text("INSERT INTO users (name, email, is_active) VALUES ('Olga', 'olga_email@gmail.com', 1)"))
    #
    # connection.commit()
    #
    result = connection.execute(text("SELECT users.email, users.name  FROM users"))

    print('+++++++++')
    #
    for row in result:
        print(row)
    #
    # print('+++++++++')
    #
    # connection.execute(text("""
    # UPDATE users
    # SET name = 'Anna Update'
    # WHERE name = 'Anna'
    # """))
    #
    # connection.commit()
    #
    #
    # result = connection.execute(text("SELECT *  FROM users"))
    #
    # print('+++++++++')
    #
    # for row in result:
    #     print(row)
    #
    # print('+++++++++')
    #
    #
    #
    # connection.execute(text("""
    # DELETE FROM users
    # WHERE name = 'Anna Update'
    # """))
    #
    # connection.commit()


    result = connection.execute(text("SELECT *  FROM users"))

    print('+++++++++')

    for row in result:
        print(row)

    print('+++++++++')

os.remove('test.db')


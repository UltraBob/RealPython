import sqlite3

with    sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("SELECT firstname, lastname from employees")

    rows = c.fetchall()
    print rows
    print rows[0]
    print rows[0][0]
    for r in rows:
        print r[0], r[1]

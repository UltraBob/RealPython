# Create a SQLite3 database and table

# import the sqlite3 library
"""import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

#insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()"""

import sqlite3
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # insert multiple records using a tuple
    cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 2700000),
            ('Houston', 'TX', 2100000),
            ('Phoenix', 'AZ', 1500000)
            ]
    # insert data into table
    c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

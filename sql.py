# sql.py - Create a SQLite3 table and populate it with data


import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect('sample.db') as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute('CREATE TABLE sampleTable(id TEXT, value TEXT)')

    # insert dummy data into the table
    c.execute('INSERT INTO sampleTable VALUES("01", "Sample value 01")')
    c.execute('INSERT INTO sampleTable VALUES("02", "Sample value 02")')
    c.execute('INSERT INTO sampleTable VALUES("03", "Sample value 03")')
    c.execute('INSERT INTO sampleTable VALUES("04", "Sample value 04")')

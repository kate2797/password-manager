# setting up DB
import sqlite3
connect_me = sqlite3.connect('database.db')
print(connect_me)

# create the table
c = connect_me.cursor()
c.execute(""" CREATE TABLE passwords
    (id PRIMARY KEY,
    username TEXT,
    password TEXT)""")
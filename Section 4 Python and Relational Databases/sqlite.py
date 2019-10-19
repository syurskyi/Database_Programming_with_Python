import sqlite3

conn = sqlite3.connect("db/helpdesl.sqlite")

if conn:
    conn.close()
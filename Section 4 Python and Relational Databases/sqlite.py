import sqlite3
from contextlib import closing

# Connect to Database
conn = sqlite3.connect("db/helpdesl.sqlite")

# Execute Select Statement
with closing(conn.cursor()) as cursor:
    cursor = conn.cursor()
    query = "SELECT * FROM employees WHERE employeeid = ?"
    cursor.execute(query, (1, ))

# Close Connection
if conn:
    conn.close()
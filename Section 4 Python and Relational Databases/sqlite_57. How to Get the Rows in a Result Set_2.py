import sqlite3
from contextlib import closing

conn = sqlite3.connect("db/helpdesk.sqlite")
conn.row_factory = sqlite3.Row

with closing(conn.cursor()) as cursor:
    query = "SELECT * FROM employees WHERE employeeid = ?"
    cursor.execute(query, (1, ))
    employee = cursor.fetchone()

    print("Name: " + employee["name"])
    print("Email: " + employee["email"])


# Close Connection
if conn:
    conn.close()
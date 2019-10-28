import sqlite3
from contextlib import closing

conn = sqlite3.connect("db/helpdesk.sqlite")

with closing(conn.cursor()) as cursor:
    query = "SELECT * FROM employees WHERE employeeid = ?"
    cursor.execute(query, (1, ))
    employee = cursor.fetchone()

    print("Name: " + employee[1])
    print("Email: " + employee[4])


# Close Connection
if conn:
    conn.close()
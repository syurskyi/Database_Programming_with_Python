import sqlite3
from contextlib import closing

conn = sqlite3.connect("db/helpdesk.sqlite")
conn.row_factory = sqlite3.Row

with closing(conn.cursor()) as cursor:
    query = "SELECT * FROM employees_roles"
    cursor.execute(query)
    employees = cursor.fetchall()

    for employee in employees:
        print("Name: " + employee["name"])
        print("Email: " + employee["email"])
        print("Role: " + employee["role"])
        print("")


# Close Connection
if conn:
    conn.close()

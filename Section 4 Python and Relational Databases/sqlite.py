import sqlite3
from contextlib import closing

# Connect to Database
conn = sqlite3.connect("db/helpdesk.sqlite")
conn.row_factory = sqlite3.Row
#
# Execute Select Statement
with closing(conn.cursor()) as cursor:
    # query = "SELECT * FROM employees WHERE employeeid = ?"
    query = "SELECT * FROM employees"
    # cursor.execute(query, (1, ))
    cursor.execute(query)
    # employee = cursor.fetchone()
    employees = cursor.fetchall()

    # print("Name: " + employee["name"])
    # print("Email: " + employee["email"])
    for employee in employees:
        print("Name: " + employee["name"])
        print("Email: " + employee["email"])
        print("")


# Close Connection
if conn:
    conn.close()
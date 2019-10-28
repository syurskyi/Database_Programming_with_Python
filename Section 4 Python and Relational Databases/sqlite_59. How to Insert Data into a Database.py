import sqlite3
from contextlib import closing

conn = sqlite3.connect("db/helpdesk.sqlite")
conn.row_factory = sqlite3.Row

# INSERT STATEMENT VARIABLES
name = "Sam"
username = 'ssuport'
password = "mypassword"
email = "sam@vectacorp.com"
roleid = 2

with closing(conn.cursor()) as cursor:
    # SELECT STATEMENT
    query = "SELECT * FROM employees_roles"
    cursor.execute(query)
    employees = cursor.fetchall()

    for employee in employees:
        print("Name: " + employee["name"])
        print("Email: " + employee["email"])
        print("Role: " + employee["role"])
        print("")

    # INSERT
    # sql = "INSERT INTO main.employees(name, username, password, email, roleid) VALUES (?, ?, ?, ?, ?) "
    # cursor.execute(sql, (name, username, password, email, roleid))
    # conn.commit()
    # print("Insert statement succeeded")



# Close Connection
if conn:
    conn.close()

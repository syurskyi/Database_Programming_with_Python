import pyodbc
from contextlib import closing

server = "localhost"
database = "vc-helpdesk"
username = "root"
password = ""
conn = pyodbc.connect("Login Prompt=False;DRIVER={Devart ODBC Driver for MySQL} ;SERVER="
                      + server +";DATABASE=" + database + ";UID=" + username + ";PWD=" + password)

# Execute Select Statements
with closing(conn.cursor()) as cursor:
    query = "SELECT * FROM employees_roles"
    cursor.execute(query)
    employees = cursor.fetchall()

    for employee in employees:
        print("Name: " + employee.name)
        print("Email: " + employee.email)
        print("Role: " + employee.role)
        print("")

if conn:
    conn.close()

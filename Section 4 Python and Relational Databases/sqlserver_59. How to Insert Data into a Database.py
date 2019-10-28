import pyodbc
from contextlib import closing

# CONNECT TO DATABASE
server = "webdb, 1400"
database = "vc-helpdesk"
username = "login_extracts"
password = ""

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}"
                      "; SERVER=" + server +
                      ";DATABASE=" + database +
                      ";UID=" + username +
                      ";PWD=" + password)

# INSERT STATEMENT VARIABLES
name = "Sam"
username = 'ssuport'
password = "mypassword"
email = "sam@vectacorp.com"
roleid = 2

# Execute Select Statements
with closing(conn.cursor()) as cursor:
    # SELECT STATEMENT
    query = "SELECT * FROM employees_roles"
    cursor.execute(query)
    employees = cursor.fetchall()

    for employee in employees:
        print("Name: " + employee.name)
        print("Email: " + employee.email)
        print("Role: " + employee.role)
        print("")

    # INSERT
    # sql = "INSERT INTO main.employees(name, username, password, email, roleid) VALUES (?, ?, ?, ?, ?) "
    # cursor.execute(sql, (name, username, password, email, roleid))
    # conn.commit()
    # print("Insert statement succeeded")

# CLOSE CONNECTION
if conn:
    conn.close()
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

# Execute Select Statements
with closing(conn.cursor()) as cursor:
    query = "SELECT * FROM employees WHERE employeeid = ?"
    cursor.execute(query, (1,))
    employee = cursor.fetchone()

    print("Name: " + employee.name)
    print("Email: " + employee.email)

# CLOSE CONNECTION
if conn:
    conn.close()
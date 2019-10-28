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
    query = "SELECT * FROM employees WHERE employeeid = ?"
    cursor.execute(query, (1,))
    employee = cursor.fetchone()

    print("Name: " + employee[1])
    print("Email: " + employee[4])

if conn:
    conn.close()

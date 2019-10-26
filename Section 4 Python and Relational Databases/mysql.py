import pyodbc

server = "localhost"
database = "vc-helpdesk"
username = "root"
password = ""
conn = pyodbc.connect("Login Prompt=False;DRIVER={MySQL ODBC 8.0 ANSI Driver}"
                      ";SERVER=" + server +
                      ";DATABASE=" + database +
                      ";UID=" + username +
                      ";PWD=" + password)
if conn:
    conn.close()

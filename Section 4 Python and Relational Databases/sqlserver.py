import pyodbc

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

# ISSUE SELECT STATEMENTS

# CLOSE CONNECTION
if conn:
    conn.close()


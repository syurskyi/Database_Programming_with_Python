import sqlite3

conn = sqlite3.connect("db/helpdesk.sqlite")

# Close Connection
if conn:
    conn.close()


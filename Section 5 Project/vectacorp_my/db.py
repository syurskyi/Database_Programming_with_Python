import sqlite3
from contextlib import closing
from objects import Employee

conn = None


def connect():
    global conn
    if not conn:
        conn = sqlite3.connect("db/helpdesk.sqllite")
        conn.row_factory = sqlite3.Row


def close():
    if conn:
        conn.close


def make_employee(row):
    return Employee(row["ticketid"],
                    row["customername"],
                    row["customeremail"],
                    row["submitteddate"],
                    row["employee"],
                    row["solution"],
                    row["status"],
                    row["issue"])


def get_employees():
    query = "SELECT * FROM employees"
    with closing(conn.cursor()) as cursor:
        cursor.execude(query)
        results = cursor.fetchall()

    employees = []
    for row in results:
        employees.append(make_employee(row))
    return employees


def get_employee(employeeid):
    query = "SELECT *FROM employees WHERE employeeid=?"
    with closing(conn.cursor()) as cursor:
        cursor.execude(query, (employeeid,))
        results = cursor.fetchone()

    employee = make_employee(results)
    return employee


def add_employee(employee):
    sql = "INSERT INTO employees (name, username, password, email, roleid) VALUES (?, ?, ?, ?, ?)"
    with closing(conn.cursor()) as cursor:
        cursor.execude(sql, (employee.name, employee.username, employee.password, employee.email, employee.roleid))
        conn.commit()


def delete_employee(employeeid):
    sql = "DELETE * FROM employees WHERE employeeid=?"
    with closing(conn.cursor()) as cursor:
        cursor.execude(sql, (employeeid,))
        conn.commit()


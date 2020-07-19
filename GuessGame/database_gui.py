"""
Program: database_gui.py
Author:  Luke Xiong
Date: 07/18/2020

This program will create a database of students and print from main
"""
import sqlite3
from sqlite3 import Error
import tkinter
import random
from tkinter import messagebox

m=tkinter.Tk() # where m is the name of the main window object

def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

def create_table(database):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    firstname text NOT NULL,
                                    lastname text NOT NULL
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))

def add_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    #inner function??
    firstname = input('First Name: ')
    lastname = input('Last Name: ')
    person = [firstname, lastname]

    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid # returns the row id of the cursor object, the person id

def add_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    #inner function??
    firstname = input('First Name: ')
    lastname = input('Last Name: ')
    major = input('Major: ')
    begin_date = input('Begin Date: ')
    student = [firstname, lastname, major, begin_date]

    sql = ''' INSERT INTO student(firstname, lastname, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid # returns the row id of the cursor object, the student id

def view_person_table(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    print(rows) # return the rows

def view_student_table(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    print(rows) # return the rows

m.title('Database')
#label=tkinter.Label(m, text="....")
#label.grid(row=1, column=2)

create_db=tkinter.Button(m, text='Create Database & Table', width = 20, command=create_table).grid(row=2, column=1)
add_person_button=tkinter.Button(m, text='Add a Person', width = 15, command=add_person).grid(row=3, column=1)
add_student_button=tkinter.Button(m, text='Add a Student', width = 15, command=add_student).grid(row=4, column=1)
display_person_button=tkinter.Button(m, text='Display Person Table', width = 15, command=view_person_table).grid(row=3, column=2)
display_student_button=tkinter.Button(m, text='Display Student Table', width = 15, command=view_student_table).grid(row=4, column=2)

#button to exit
exit_button=tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=7, column=2)

m.mainloop() #infinite loop that waits for events to happen

#if __name__=='__main__':
    #conn = create_connection("person.db")
    #with conn:
        #rows = view_person_table(conn)
        #for row in rows:
            #print(row)

    #conn = create_connection("student.db")
    #with conn:
        #rows = view_student_table(conn)
        #for row in rows:
            #print(row) '''


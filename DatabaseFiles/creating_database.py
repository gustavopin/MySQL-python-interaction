import mysql.connector

# connecting to the mysql server
school_database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'rootpassword'
)

# creating a cursor
school_cursor = school_database.cursor()

# creating the database
school_cursor.execute('CREATE DATABASE SchoolGrades')
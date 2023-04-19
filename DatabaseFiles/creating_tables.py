import mysql.connector

# connecting to the mysql server
school_database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'rootpassword',
    database = 'SchoolGrades'
)

# creating a cursor
school_cursor = school_database.cursor()        #cursor is a temporary memory used to store database tables

# creating a table with students information
# after the table is created, insert a tag in the line below
school_cursor.execute('CREATE TABLE student (name VARCHAR(100), student_number int PRIMARY KEY AUTO_INCREMENT, age smallint UNSIGNED)')

# creating a table with student grades
# after the table is created, insert a tag in the line below
school_cursor.execute('CREATE TABLE grades (p1 smallint, p2 smallint, p3 smallint, p4 smallint)')
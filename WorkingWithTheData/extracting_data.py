import mysql.connector
import pandas as pd

# connecting to the mysql server
school_database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'rootpassword',
    database = 'SchoolGrades'
)

# creating a cursor
school_cursor = school_database.cursor()

# selecting the wanted elements
school_data_query1 = 'SELECT student_number, name, age FROM student'

# executing the select
school_cursor.execute(school_data_query1)

# creating a lists to future storage
student_id = []
student_name = []
student_age = []

# fetching and printing the data
school_students = school_cursor.fetchall()

for student in school_students:
    student_id.append(student[0])
    print(f'Student ID = ', student[0])
    student_name.append(student[1])
    print(f'Student Name = ', student[1])
    student_age.append(student[2])
    print(f'Student Age = ', student[2], '\n')

# creating a dictionary
dt1 = pd.DataFrame({
    'Student ID' : student_id,
    'Student Name' : student_name,
    'Student Age' : student_age
})

# query for student grades
school_data_query2 = 'SELECT student_number, p1, p2, p3, p4 FROM grades'

# executing the query
school_cursor.execute(school_data_query2)

#creating lists for storage
p1 = []
p2 = []
p3 = []
p4 = []

# fetching data from grades table and printing it
school_grades = school_cursor.fetchall()

for grade in school_grades:
    print('Student ID = ', grade[0])
    p1.append(grade[1])
    print('First test = ', grade[1])
    p2.append(grade[2])
    print('Second test = ', grade[2])
    p3.append(grade[3])
    print('Third test = ', grade[3])
    p4.append(grade[4])
    print('Fourth test = ', grade[4], '\n')

# creating a dictionary
dt2 = pd.DataFrame ({
    'Student ID' : student_id,
    'Test 1' : p1,
    'Test 2' : p2,
    'Test 3' : p3,
    'Test 4' : p4
})
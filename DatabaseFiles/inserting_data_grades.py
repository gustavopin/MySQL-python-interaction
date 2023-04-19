import mysql.connector

# connecting to the mysql server
school_database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'rootpassword',
    database = 'SchoolGrades'
)

# creating a cursor
school_cursor = school_database.cursor()

# inserting data in the 'grades' table
sql_insert2 = 'INSERT INTO grades (p1, p2, p3, p4) VALUES (%s, %s, %s, %s)'
values2 = [
    ('10', '9', '8', '10'),
    ('9', '9', '10', '10'),
    ('7', '10', '6', '9'),
    ('4', '8', '9', '7'),
    ('7', '6', '8', '9'),
    ('7', '8', '9', '10'),
    ('2', '4', '6', '8'),
    ('10', '9', '8', '7'),
    ('1', '4', '7', '2'),
    ('7', '5', '8', '8'),
    ('7', '7', '7', '7'),
    ('8', '9', '10', '10'),
    ('9', '9', '9', '9'),
    ('7', '6', '5', '7'),
    ('10', '9', '10', '9'),
    ('6', '10', '7', '5'),
    ('6', '8', '10', '7'),
    ('8', '7', '6', '7'),
    ('6', '7', '10', '9'),
    ('7', '2', '8', '5')
]

# executing the cursor
school_cursor.executemany(sql_insert2, values2)

# MySQL commit
school_database.commit()

# print for testing
print(school_cursor.rowcount, 'was inserted')
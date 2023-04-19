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

# inserting data in the 'student' table
sql_insert1 = 'INSERT INTO student (name, age) VALUES (%s, %s)'
values = [
    ('Mack Nem Cheese', '10'),
    ('Ana Missu', '11'),
    ('Rodrick Godfrey', '10'),
    ('Lance Reed', '14'),
    ('Monique Glad', '15'),
    ('Sonya Barb', '11'),
    ('Lee Pine', '13'),
    ('Theodora Young', '11'),
    ('Robert Downiro', '10'),
    ('Clover Fourth', '12'),
    ('Hope Arno', '15'),
    ('Sanic Link', '11'),
    ('Luke Skyrunner', '15'),
    ('Cory Water', '13'),
    ('Gus Oak', '12'),
    ('Lory Silva', '10'),
    ('Pedro Vski', '11'),
    ('Jean Stock', '15'),
    ('Lon Glon', '14'),
    ('Rick Mort', '14')
]

# executing the cursor
school_cursor.executemany(sql_insert1, values)

# MySQL commit
school_database.commit()

# print for testing
print(school_cursor.rowcount, 'was inserted')
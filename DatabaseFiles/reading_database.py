import mysql.connector

# this is a test to see if the database was really created
# connecting to the database
school_database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'rootpassword',
    database = 'SchoolGrades'  # the code can read the database from here insted of creating a cursor for it, but can't print any results
)                              # if you run the code without the lines of code below and it doesn`t present a error, that means the database is ok

# creating a cursor
school_cursor = school_database.cursor()

# reading the database
school_cursor.execute("SHOW DATABASES")

# printing the contents of the database
for x in school_cursor:
  print(x)
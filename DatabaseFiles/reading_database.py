import mysql.connector

# connecting to the database
school_database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'rootpassword',
    database = 'SchoolGrades'  # the code can read the database from here insted of creating a cursor for it, but can't print any results
)

# creating a cursor
school_cursor = school_database.cursor()

# reading the database
school_cursor.execute("SHOW DATABASES")

# printing the contents of the database
for x in school_cursor:
  print(x)
import mysql.connector

# connecting to the mysql server
school_database = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'rootpassword',
    database = 'SchoolGrades'
)

# creating the cursor
school_cursor = school_database.cursor()

# deleting items from the database
# deleting a whole table
# remove the tag and change the statment after 'DROP TABLE'
#school_del_table = 'DROP TABLE student'

#school_cursor.execute(school_del_table)

# deleting rows
# remove the tag and change 'table_name', 'column' and 'wanted_row' with your data
#school_del_row = 'DELETE FROM table_name WHERE column = wanted_row'

#school_cursor.execute(school_del_row)

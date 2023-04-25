# Database Creation with Python

This project extend the knowledge of python programming while inserting SQL commands to communicate with a local server created from MySQL.
It involves creating databases, tables, inserting and extracting elements so they can be organized in a visually pleasent way.

## Phase 1

- This phase is the creation of the MySQL connection with the MySQL Workbench. This allow the creation of databases inside this connections to store the data within its tables.
    - The creation of the database can be found in the file 'creating_database.py'.
    - The creation of the tables can be found in the file 'creating_table.py'.
    - A code to test if the database is working, it is inside the file 'reading_database.py'.
    - There is a code named 'deleting_items.py' that deletes the whole table or a specific column of the database.

## Phase 2

- Create and insert data within the databases created.
    - Insertion of students info.
    - Insertion of students grades.
        - Both can be found in the folder DatabaseFiles under the names 'inserting_data_grades' and 'inserting_data_names'.
    
## Phase 3

- Extract the data from the database and organize it.
    - This can be found in the file 'extracting_data.py'.
    - This creates a xlsx file with the name 'student_info'. The file is inside the folder WorkingWithTheData.

## Phase 4

- Working with the data.
    - This can be found in the file 'data_analysis.py'.
    - This phase creates:
        - Table of average grades.
        - Table of students under the average grade (in this case 7).
        - Pie graph of the percentage of 'Above Minimum Grade' and 'Below Minimum Grade' values.
        - Bar graph of all the average grades of the students (with the names in the X axis).
        - Two Matrix Correlations, the first one comparing all the test (1 through 4) and the second comparing Age and the Average Grade.
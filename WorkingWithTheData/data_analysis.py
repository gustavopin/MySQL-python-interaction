import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

# reading the xlsx file
data1 = pd.read_excel('Project4\WorkingWithTheData\student_info.xlsx', sheet_name = 'StudentID')
data2 = pd.read_excel('Project4\WorkingWithTheData\student_info.xlsx', sheet_name = 'Grades')

# creating lists
names = data1['Student Name'].tolist()
age = data1['Student Age'].tolist()
studentID = data1['Student ID'].tolist()
p1 = data2['Test 1'].tolist()
p2 = data2['Test 2'].tolist()
p3 = data2['Test 3'].tolist()
p4 = data2['Test 4'].tolist()

# average grade for the students
sum_grades = [w + x + y + z for w, x, y, z in zip(p1, p2, p3, p4)]
average_grade = [x / 4 for x in sum_grades]

# creating a dictionary with the average grades of the students
df1 = pd.DataFrame({
    'Average Grade' : average_grade
})



# updating the xlsx file with the new dataframe
# THIS IS REWRITING THE xlsx FILE, NEED TO WORK ON THAT
#data2['Average Grades'] = df1

#writer = pd.ExcelWriter('Project4\WorkingWithTheData\student_info.xlsx')
#data2.to_excel(writer, index = False)
#writer.save()
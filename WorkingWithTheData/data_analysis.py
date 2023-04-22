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
df1 = pd.DataFrame({'Average Grade' : average_grade})

# storing the grades inside the xlsx file
wb = load_workbook('Project4\WorkingWithTheData\student_info.xlsx')
ws = wb['Grades']

for index, row in df1.iterrows(): #still working on this
    cell = 'C%d' % (index + 5)
    ws[cell] = row[0]

wb.save()
import pandas as pd
import matplotlib.pyplot as plt

# reading the xlsx file
data1 = pd.read_excel('Project4\WorkingWithTheData', sheet_name = 'StudentID')
data2 = pd.read_excel('Project4\WorkingWithTheData', sheet_name = 'Grades')

# creating lists
names = data1['Student Name'].tolist()
age = data1['Student Age'].tolist()
studentID = data1['Student ID'].tolist()
p1 = data2['Test 1'].tolist()
p2 = data2['Test 2'].tolist()
p3 = data2['Test 3'].tolist()
p4 = data2['Test 4'].tolist()

# average grade for the students

import pandas as pd
import matplotlib.pyplot as plt


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
    'Student ID' : studentID,
    'Student Name' : names,
    'Student Age' : age,
    'Test 1' : p1,
    'Test 2' : p2,
    'Test 3' : p3,
    'Test 4' : p4,
    'Average Grade' : average_grade
})

# slecting the students with below average grades
below_average = df1[df1['Average Grade'] < 7]
print(below_average)       

# counting the students above and below the minimum grade
    # below
std_blw_min = 0
for x in average_grade:
    if x < 7:
        std_blw_min += 1
    
    #above
std_abv_min = 0
for y in average_grade:
    std_abv_min += 1
std_abv_min = std_abv_min - std_blw_min
    
    # results
print(f'\nStudents above the minimum grade: {std_abv_min}')
print(f'Students below the minimum grade: {std_blw_min}')

    # graph
    # list with objects
std_abv_blw = [std_abv_min, std_blw_min]
labels_g1 = ['Above Minimum', 'Below Minimum']
colors_g1 = ['lightskyblue', 'lightcoral']
explode_g1 = (0, 0.1)

    # ploting the graph
plt.pie(std_abv_blw, labels = labels_g1, shadow = True, autopct = '%1.1f%%', colors = colors_g1, explode = explode_g1)
plt.show()

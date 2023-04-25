import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


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
print(f'Students below the minimum grade: {std_blw_min}\n')


# average grade per test
    # summing the number of grades
number_students = 0
for student in studentID:
    number_students += 1

    # test1
sum_p1 = 0
for grade in p1:
    sum_p1 = sum_p1 + grade
average_p1 = sum_p1 / number_students

    # test 2
sum_p2 = 0
for grade in p2:
    sum_p2 = sum_p2 + grade
average_p2 = sum_p2 / number_students

    # test 3
sum_p3 = 0
for grade in p3:
    sum_p3 = sum_p3 + grade
average_p3 = sum_p3 / number_students

    # test 4
sum_p4 = 0
for grade in p4:
    sum_p4 = sum_p4 + grade
average_p4 = sum_p4 / number_students

    # creating a dataframe for the average of every test
average_tests = pd.DataFrame({
    "Average Test 1" : average_p1,
    "Average Test 2" : average_p2,
    "Average Test 3" : average_p3,
    "Average Test 4" : average_p4
}, index = [0])

print(average_tests)

# creating graphs
    # list with objects
std_abv_blw = [std_abv_min, std_blw_min]
labels_g1 = ['Above Minimum', 'Below Minimum']
colors_g1 = ['lightskyblue', 'lightcoral']
explode_g1 = (0, 0.1)

    # ploting the graph
        #pie
plt.pie(std_abv_blw, labels = labels_g1, shadow = True, autopct = '%1.1f%%', colors = colors_g1, explode = explode_g1)
plt.show()

        #bar
plt.bar(names, average_grade, color = 'grey', width = 0.2)
plt.xlabel('Student ID')
plt.ylabel('Grades')
plt.title('Average Student Grade')
plt.xticks(rotation = 90)
plt.show()

# working with correlation matrix
    # creating a new dataframe for grades
df2 = pd.DataFrame({
    'Test 1' : p1,
    'Test 2' : p2,
    'Test 3' : p3,
    'Test 4' : p4
})

        # correlation matrix (tests)
matrix1 = df2.corr()
sn.heatmap(matrix1, annot = True, cmap = 'coolwarm')
plt.show()

    # creating a new dataframe for age/average grades
df3 = pd.DataFrame({
    'Age' : age,
    'Average Grade' : average_grade,
})
        # correlation matrix (age/average grades)

matrix2 = df3.corr()
sn.heatmap(matrix2, annot = True, cmap = 'coolwarm')
plt.show()
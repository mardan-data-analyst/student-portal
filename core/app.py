from core.model.Student import Student
from core.model.checker import gradeStudent, isPassed

import pandas as pd

#Empty lists are created we will need them later
passed_students = []
failed_students = []

# We are taking number of students will be in our list
try:
    iterations = int(input("Please enter number of iterations: "))
except:
    # in case if there is not correct type inserted we will throw this error
    raise TypeError("Type is not correct")
for i in range(iterations):
    # we are starting to take inputs from user
    try:
        print('------')
        name = input("Name: ")
        surname = input("Surname: ")
        schoolNo = input("schoolNo: ")
        point = int(input("Point: "))
        #We are creating our model
        student  = Student(name, surname, schoolNo, point, isPassed(gradeStudent(point)))
        #We are checking if the student is passed or not,, then we are adding them to their corresponding lists
        if student.passed:
            passed_students.append(student)
        else:
            failed_students.append(student)
    except:
        raise TypeError("Type is not correct")



# We are converting list of students to DF then print and save it csv file
df_passed = pd.DataFrame([t.__dict__ for t in passed_students])
df_passed = df_passed.loc[:, df_passed.columns!='passed']
print('Passed Students')
print(df_passed)
df_passed.to_csv('passed_students.csv')


print('------')
df_failed = pd.DataFrame([t.__dict__ for t in failed_students])
df_failed = df_failed.loc[:, df_failed.columns !='passed']
df_failed.to_csv('failed_students.csv')
print('Failed Students')
print(df_failed)
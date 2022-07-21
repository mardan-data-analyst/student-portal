from core.model.Student import Student
from core.model.checker import gradeStudent, isPassed
import pandas as pd

#Empty lists are created we will need them later
passed_students = []
failed_students = []

df = pd.read_csv('Math_Results.csv', skipinitialspace=True)
# See the keys
for i in range(0, df.values.size):
    row = df.values[i][0].split(";")

    # We are creating our model
    student  = Student(row[0], row[1], row[2], int(row[3]), isPassed(gradeStudent(int(row[3]))))
    #We are checking if the student is passed or not,, then we are adding them to their corresponding lists
    if student.passed:
         passed_students.append(student)
    else:
        failed_students.append(student)




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
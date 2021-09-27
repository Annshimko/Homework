# Task 5.3
# File data/students.csv stores information about students in CSV format.
# This file contains the student’s names, age and average mark.
# Implement a function which receives file path and returns names of top performer students

import pandas as pd


def get_top_performers(file_path, number_of_top_students=5):
    students = pd.read_csv(file_path)
    return list(
        students.sort_values(
            by='average mark', ascending=False).head(number_of_top_students)['student name'])


def sort_students_age(file_path):
    students = pd.read_csv(file_path)
    students.sort_values(by='age', ascending=False).to_csv('data/sorted_by_age.csv', index=False)


filepath = "data\students.csv"

print(get_top_performers(filepath))
sort_students_age(filepath)

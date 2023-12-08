# Zala Weyker
# 12/4/2023
# Evaluation
# This program asks for a notes file, adds up total points recieved for each student, then prints a simple report sorting all students alphabetically.
# This file should be baby-proofed
import os

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, errline):
        self.line = errline

    def __str__(self):
        return f"The file is incorrectly formatted in line {line}."


class FieldErr(BadLine):
    def __str__(self):
        return f"There are not enough fields in line {self.line}. There should be a first name, a last name, and a score"


class Badnum(BadLine):
    def __str__(self):
        return f"The score in line {line} is not a valid number."

class FileEmpty(StudentsDataException):
    def __str__(self):
        return "The file is empty"


file_name = input("what is the name of the file")
students={}

try:
    with open(file_name, 'r') as notes:
        if os.path.getsize(file_name) == 0:
            raise FileEmpty
        for count, line in enumerate(notes):
            try:
                fln = line.split()
                first = fln[0]
                last = fln[1]
                number = fln[2]
                if f'{first} {last}' in students:
                    students[f'{first} {last}'] += float(number)
                else:
                    students[f'{first} {last}'] = float(number)
            except IndexError:
                raise FieldErr(count)
            except ValueError:
                raise Badnum(count)
except FileNotFoundError:
    print("I couldn't find that file")
    raise

def report_students(student_dir):
    reportlines=[]
    for student in student_dir:
        reportlines.append(f"{student:15}{student_dir[student]}")
    for reportline in sorted(reportlines):
        yield reportline

for score in report_students(students):
    print(score)

# DataLayer.py
#Alejandro Fonseca Exam 2

import csv

DATA_PATH = "/"
DATA_READER = False


def read_csv(file_name):
    if not DATA_READER:
        return []
    with open(DATA_PATH + file_name, mode='r') as file:
        return list(csv.DictReader(file))


def append_csv(file_name, fieldnames, rows):
    with open(DATA_PATH + file_name, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def get_students():
    return read_csv("students.csv")


def get_classes():
    return read_csv("class.csv")


def get_instructor():
    return read_csv("instructor.csv")


def get_instructors():
    return read_csv("instructors.csv")


def get_grades():
    return read_csv("grades.csv")


def get_scholarships():
    return read_csv("scholarships.csv")

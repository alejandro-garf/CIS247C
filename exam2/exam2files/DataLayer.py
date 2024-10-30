# DataLayer.py
#Alejandro Fonseca Exam 2

import csv

DATA_PATH = "data/"
DATA_READER = True


def read_csv(file_name):
    if not DATA_READER:
        return []
    try:
        with open(DATA_PATH + file_name, mode='r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: Could not find {file_name} in {DATA_PATH}")
        return []


def append_csv(file_name, fieldnames, row):
    try:
        with open(DATA_PATH + file_name, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(row)  # Write only the new row
        return True
    except Exception as e:
        print(f"Error appending to {file_name}: {str(e)}")
        return False


def get_students():
    return read_csv("students.csv")


def get_classes():
    return read_csv("classes.csv")


def get_instructor():
    return read_csv("instructors.csv")


def get_instructors():
    return read_csv("instructors.csv")


def get_grades():
    return read_csv("grades.csv")


def get_scholarships():
    return read_csv("scholarships.csv")

# StudentProcess.py
#Alejandro Fonseca Exam 2

from DataLayer import get_students, get_classes, get_instructor, get_instructors, get_grades, get_scholarships, \
    append_csv
from DataFormatter import format_past_classes, format_scholarships, format_student_profile, format_gpa_calculation


def get_class_overview():
    classes = get_classes()
    instructors = get_instructor()
    if not classes or not instructors:
        return {"columns": {}, "data": []}

    #Create a lookup directory for the instructor
    instructor_dict = {i["InstructorID"]: i for i in instructors}

    class_overview_data = []
    for class_info in classes:
        instructor = instructor_dict.get(class_info["InstructorID"], {})
        class_data = {
            "ClassName": class_info["ClassName"],
            "Credits": class_info["Credits"],
            "ClassType": class_info["ClassType"],
            "Instructor": instructor.get("Name", "Unknown"),
            "ClassID": class_info["ClassID"]
        }
        class_overview_data.append(class_data)

    #Define Columns
    columns = {
        "ClassName": "ClassName",
        "Credits": "Credits",
        "ClassType": "ClassType",
        "Instructor": "Instructor"
    }

    return {"columns": columns, "data": class_overview_data}


def get_students_enrolled_in_class(class_id):
    grades = get_grades()
    students = get_students()

    # Convert class_id to string
    class_id = str(class_id)

    # Get all students who are enrolled
    enrolled_students = []

    # Create a lookup dictionary for students
    student_dict = {str(s["StudentID"]): s for s in students}

    # Find all students enrolled in this class
    for grade in grades:
        if str(grade["ClassID"]) == class_id and not grade["Grade"]:  # No grade means currently enrolled
            student_id = str(grade["StudentID"])
            if student_id in student_dict:
                enrolled_students.append(student_dict[student_id])

    return enrolled_students


def calculate_gpa(student_id, semester=None):
    grades = get_student_past_classes(student_id)
    total_points = sum(_grade_to_points(g["Grade"]) for g in grades if g["Grade"])
    grade_count = sum(1 for g in grades if g["Grade"])

    return round(total_points / grade_count, 2) if grade_count > 0 else None


def get_instructor_info(class_id):
    instructors = get_instructors()
    classes = get_classes()
    class_info = next((c for c in classes if c["ClassID"] == class_id), None)
    if class_info:
        instructor_id = class_info["InstructorID"]
        return next((i for i in instructors if i["InstructorID"] == instructor_id), None)
    return None


def check_scholarship_eligibility(student_id):
    gpa = calculate_gpa(student_id)
    if gpa is None:
        return []

    scholarships = get_scholarships()
    eligible_scholarships = [s for s in scholarships if gpa >= float(s["GPARequirement"])]
    return eligible_scholarships


def get_student_profile(student_id):
    students = get_students()
    student = next((s for s in students if s["StudentID"] == student_id), None)

    if student:
        student["Grades"] = get_student_past_classes(student_id)
    else:
        return None

    return student


def historical_analysis(student_id):
    grades = get_student_past_classes(student_id)
    year_grades = {}

    for g in grades:
        year = g["Year"]
        if year not in year_grades:
            year_grades[year] = []
        year_grades[year].append(_grade_to_points(g["Grade"]))

    trends = []
    previous_gpa = None

    for year in sorted(year_grades.keys()):
        current_gpa = round(sum(year_grades[year]) / len(year_grades[year]), 2)
        if previous_gpa:
            if current_gpa > previous_gpa:
                trends.append(f"Improved in {year}")
            elif current_gpa < previous_gpa:
                trends.append(f"Declined in {year}")
            else:
                trends.append(f"Consistent in {year}")
        previous_gpa = current_gpa

    return trends if trends else ["No performance data available."]


def course_progression_tracking(student_id):
    grades = get_student_past_classes(student_id)
    classes = get_classes()

    core_classes = {c["ClassID"]: c for c in classes if c["ClassType"] == "Core"}
    electives = {c["ClassID"]: c for c in classes if c["ClassType"] == "Elective"}

    core_taken = [g["ClassID"] for g in grades if g["ClassID"] in core_classes]
    electives_taken = [g["ClassID"] for g in grades if g["ClassID"] in electives]

    core_progress = f"Core classes taken: {len(core_taken)} / {len(core_classes)}"
    elective_progress = f"Electives taken: {len(electives_taken)}"

    return {"Core Progress": core_progress, "Elective Progress": elective_progress}


def elective_analysis(student_id):
    grades = get_student_past_classes(student_id)
    classes = get_classes()

    elective_classes = {c["ClassID"]: c for c in classes if c["ClassType"] == "Elective"}
    elective_grades = [g for g in grades if g["ClassID"] in elective_classes]

    if not elective_grades:
        return {"Message": "No elective courses taken."}

    average_grade = sum(_grade_to_points(g["Grade"]) for g in elective_grades) / len(elective_grades)
    return {
        "Electives Taken": len(elective_grades),
        "Average Elective Grade": round(average_grade, 2)
    }


def get_all_classes():
    return get_classes()


def add_future_class(student_id, class_id, semester, year):
    valid_semesters = {"Fall", "Spring", "Summer"}
    if semester not in valid_semesters or not year.isdigit():
        raise ValueError("Invalid semester or year.")

    grades = get_grades()
    if any(g["StudentID"] == student_id and g["ClassID"] == class_id for g in grades):
        return "Record already exists"

    students = get_students()
    if not any(student["StudentID"] == student_id for student in students):
        return "Student does not exist"

    new_row = {
        "StudentID": student_id,
        "ClassID": class_id,
        "Grade": "",
        "Year": year,
        "Semester": semester,
        "Exam1": "", "Exam2": "", "Assignments": ""
    }
    grades.append(new_row)
    fieldnames = new_row.keys()
    append_csv("grades.csv", fieldnames, grades)
    return "Success"


def get_student_past_classes(student_id):
    grades = get_grades()
    classes = get_classes()
    student_grades = [g for g in grades if g["StudentID"] == student_id]
    for grade in student_grades:
        class_info = next((c for c in classes if c["ClassID"] == grade["ClassID"]), {})
        grade["ClassName"] = class_info.get("ClassName", "Unknown")
    return student_grades


def get_student_grades_report():
    grades = get_grades()
    students = get_students()
    classes = get_classes()
    report = []

    for grade in grades:
        if not grade["Grade"]:
            continue

        student = next((s for s in students if s["StudentID"] == grade["StudentID"]), {})
        class_info = next((c for c in classes if c["ClassID"] == grade["ClassID"]), {})
        report.append({
            "StudentID": grade["StudentID"],
            "Name": student.get("Name", ""),
            "ClassName": class_info.get("ClassName", ""),
            "Grade": grade["Grade"],
            "Year": grade["Year"]
        })
    return report


def get_classes_with_instructors():
    classes = get_classes()
    instructors = get_instructors()
    data = []

    for c in classes:
        instructor = next((i for i in instructors if i["InstructorID"] == c["InstructorID"]), {})
        data.append({
            "ClassID": c["ClassID"],
            "ClassName": c["ClassName"],
            "Credits": c["Credits"],
            "Instructor": instructor.get("Name", "Unknown"),
            "Department": instructor.get("Department", "Unknown")
        })
    return data


def get_students_eligible_for_scholarships():
    students = get_students()
    scholarships = get_scholarships()
    eligible_students = []
    for student in students:
        gpa = calculate_gpa(student["StudentID"])
        if gpa is None:
            continue

        student_scholarships = [
            s["Name"] for s in scholarships if gpa >= float(s["GPARequirement"])
        ]

        if student_scholarships:
            eligible_students.append({
                "StudentID": student["StudentID"],
                "Name": student["Name"],
                "GPA": gpa,
                "Scholarship": ", ".join(student_scholarships)
            })

    return eligible_students


def _grade_to_points(grade):
    points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    return points.get(grade, 0.0)


def get_completed_classes(student_id, grades=None):
    grades = get_grades()
    classes = get_classes()

    completed_classes = [g for g in grades if g["StudentID"] == student_id and g["Grade"]]

    for grade in completed_classes:
        class_info = next((c for c in classes if c["ClassID"] == grade["ClassID"]), {})
        grade["ClassName"] = class_info.get("ClassName", "Unknown")
        grade["Credits"] = class_info.get("Credits", "Unknown")

    return completed_classes

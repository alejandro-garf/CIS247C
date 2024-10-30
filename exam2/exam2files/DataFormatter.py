# DataFormatter.py
#Alejandro Fonseca Exam 2

def format_past_classes(student_grades):
    if not student_grades:
        return "No past classes found."

    formatted_result = ""
    for item in student_grades:
        formatted_result += f"Class: {item.get('ClassName', 'N/A')}\n"
        formatted_result += f"Grade: {item.get('Grade', 'N/A')}\n"
        formatted_result += f"Year: {item.get('Year', 'N/A')}\n"
        formatted_result += f"Semester: {item.get('Semester', 'N/A')}\n"
        formatted_result += f"Exam 1: {item.get('Exam1', 'N/A')}\n"
        formatted_result += f"Exam 2: {item.get('Exam2', 'N/A')}\n"
        formatted_result += f"Assignments: {item.get('Assignments', 'N/A')}\n"
        formatted_result += "-" * 40 + "\n"
    return formatted_result


def format_gpa_calculation(grades):
    if not grades:
        return "No grades available for GPA calculation."

    formatted_result = "Grades Used in GPA Calculation:\n\n"
    for grade in grades:
        formatted_result += f"Class: {grade.get('ClassName', 'N/A')}\n"
        formatted_result += f"Grade: {grade.get('Grade', 'N/A')}\n"
        formatted_result += f"Year: {grade.get('Year', 'N/A')}\n"
        formatted_result += f"Semester: {grade.get('Semester', 'N/A')}\n"
        formatted_result += "-" * 40 + "\n"
    return formatted_result


def format_scholarships(eligible_scholarships):
    if not eligible_scholarships:
        return "No eligible scholarships found."

    formatted_result = ""
    for scholarship in eligible_scholarships:
        formatted_result += f"Scholarship: {scholarship.get('Name', 'N/A')}\n"
        formatted_result += f"GPA Requirement: {scholarship.get('GPARequirement', 'N/A')}\n"
        formatted_result += "-" * 40 + "\n"
    return formatted_result


def format_student_profile(profile):
    if not profile:
        return "No profile information available."

    formatted_profile = f"Profile for Student ID {profile.get('StudentID', 'N/A')}:\n\n"
    formatted_profile += f"Name: {profile.get('Name', 'N/A')}\n"
    formatted_profile += f"Age: {profile.get('Age', 'N/A')}\n"
    formatted_profile += f"Major: {profile.get('Major', 'N/A')}\n"
    formatted_profile += "Grades:\n"

    for grade in profile.get("Grades", []):
        formatted_profile += (
            f"- Class: {grade.get('ClassName', 'N/A')}, Grade: {grade.get('Grade', 'N/A')}, "
            f"Year: {grade.get('Year', 'N/A')}, Semester: {grade.get('Semester', 'N/A')}\n"
        )

    return formatted_profile

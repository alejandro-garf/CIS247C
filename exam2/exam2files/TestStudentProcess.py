# TestStudentProcess.py
#Alejandro Fonseca Exam 2

import unittest
from unittest.mock import patch
from StudentProcess import calculate_gpa, get_student_profile, add_future_class, check_scholarship_eligibility, \
    get_students_eligible_for_scholarships


class TestGPA(unittest.TestCase):
    """Tests related to GPA calculations without using credits."""

    @patch('StudentProcess.get_student_past_classes')
    def test_calculate_gpa_valid(self, mock_get_grades):
        mock_get_grades.return_value = [
            {"ClassID": "101", "Grade": "A"},
            {"ClassID": "102", "Grade": "B"}
        ]
        gpa = calculate_gpa("1")
        self.assertAlmostEqual(gpa, 3.5, places=2)

    @patch('StudentProcess.get_student_past_classes')
    def test_calculate_gpa_no_grades(self, mock_get_grades):
        mock_get_grades.return_value = []  # No grades
        gpa = calculate_gpa("2")
        self.assertIsNone(gpa)

    @patch('StudentProcess.get_student_past_classes')
    def test_calculate_gpa_some_invalid_grades(self, mock_get_grades):
        mock_get_grades.return_value = [
            {"ClassID": "101", "Grade": "A"},
            {"ClassID": "102", "Grade": None}  # Invalid grade
        ]
        gpa = calculate_gpa("3")
        self.assertAlmostEqual(gpa, 4.0, places=2)


class TestStudentProfile(unittest.TestCase):
    """Tests related to student profile retrieval."""

    @patch('StudentProcess.get_students')
    @patch('StudentProcess.get_student_past_classes')
    def test_valid_student_profile(self, mock_get_grades, mock_get_students):
        mock_get_students.return_value = [
            {"StudentID": "1", "Name": "John Doe", "Age": "20", "Major": "Computer Science"}
        ]
        mock_get_grades.return_value = [
            {"ClassID": "101", "ClassName": "Math", "Grade": "A"}
        ]
        profile = get_student_profile("1")
        self.assertEqual(profile["Name"], "John Doe")
        self.assertEqual(len(profile["Grades"]), 1)

    @patch('StudentProcess.get_students')
    def test_invalid_student_id(self, mock_get_students):
        mock_get_students.return_value = []
        profile = get_student_profile("999")
        self.assertIsNone(profile)

    @patch('StudentProcess.get_students')
    @patch('StudentProcess.get_student_past_classes')
    def test_student_with_no_grades(self, mock_get_grades, mock_get_students):
        mock_get_students.return_value = [
            {"StudentID": "2", "Name": "Jane Smith", "Age": "21", "Major": "Biology"}
        ]
        mock_get_grades.return_value = []  # No classes
        profile = get_student_profile("2")
        self.assertEqual(profile["Name"], "Jane Smith")
        self.assertEqual(profile["Grades"], [])


class TestClassAddition(unittest.TestCase):

    @patch('StudentProcess.get_grades')
    @patch('StudentProcess.append_csv')
    def test_successful_class_addition(self, mock_append_csv, mock_get_grades):
        # Mock initial grades data
        mock_get_grades.return_value = [
            {"StudentID": "1", "ClassID": "100", "Grade": "A", "Year": "2023", "Semester": "Spring"}
        ]

        # Add a new class
        add_future_class("1", "101", "Fall", "2024")

        # Assert append_csv was called with new data
        mock_append_csv.assert_called_once()
        updated_grades = mock_append_csv.call_args[0][2]
        self.assertIn({"StudentID": "1", "ClassID": "101", "Grade": "", "Year": "2024", "Semester": "Fall",
                       "Exam1": "", "Exam2": "", "Assignments": ""}, updated_grades)

    @patch('StudentProcess.get_grades')
    def test_duplicate_class_addition(self, mock_get_grades):
        mock_get_grades.return_value = [
            {"StudentID": "1", "ClassID": "101", "Grade": "A", "Year": "2023", "Semester": "Spring"}
        ]

        # Try adding the same class again
        result = add_future_class("1", "101", "Fall", "2024")

        # Assert that the duplicate class wasn't added
        self.assertIsNone(result)

    @patch('StudentProcess.get_grades')
    def test_invalid_student_id(self, mock_get_grades):
        mock_get_grades.return_value = []

        # Attempt to add class with invalid student ID
        result = add_future_class("999", "101", "Fall", "2024")

        # Assert that invalid student ID is handled gracefully
        self.assertIsNone(result)

    def test_invalid_semester_or_year(self):
        # Add with invalid semester and year combinations
        with self.assertRaises(ValueError):
            add_future_class("1", "102", "InvalidSemester", "2024")

        with self.assertRaises(ValueError):
            add_future_class("1", "102", "Fall", "InvalidYear")


class TestScholarshipEligibility(unittest.TestCase):
    def setUp(self):
        # Mock sample data for scholarships
        self.mock_scholarships = [
            {"ScholarshipID": "1", "Name": "Merit Scholarship", "GPARequirement": "3.5"},
            {"ScholarshipID": "2", "Name": "Excellence Award", "GPARequirement": "3.75"},
        ]

        # Mock sample student data
        self.mock_students = [
            {"StudentID": "1", "Name": "John Doe", "GPA": 3.8},
            {"StudentID": "2", "Name": "Jane Smith", "GPA": 3.3},
        ]

    @patch('StudentProcess.get_scholarships', return_value=[
        {"ScholarshipID": "1", "Name": "Merit Scholarship", "GPARequirement": "3.5"},
        {"ScholarshipID": "2", "Name": "Excellence Award", "GPARequirement": "3.75"}
    ])
    @patch('StudentProcess.calculate_gpa', return_value=3.8)
    def test_check_scholarship_eligibility_valid_gpa(self, mock_calculate_gpa, mock_get_scholarships):
        eligible_scholarships = check_scholarship_eligibility("1")

        # Assert the student is eligible for both scholarships
        self.assertEqual(len(eligible_scholarships), 2)  # John Doe should be eligible for both

    @patch('StudentProcess.get_scholarships', return_value=[
        {"ScholarshipID": "1", "Name": "Merit Scholarship", "GPARequirement": "3.5"},
    ])
    def test_check_scholarship_eligibility_ineligible_gpa(self, mock_get_scholarships):
        eligible_scholarships = check_scholarship_eligibility("2")  # Jane Smith has 3.3 GPA
        self.assertEqual(len(eligible_scholarships), 0)

    @patch('StudentProcess.get_scholarships', return_value=[])
    def test_no_scholarships_available(self, mock_get_scholarships):
        eligible_scholarships = check_scholarship_eligibility("1")
        self.assertEqual(len(eligible_scholarships), 0)

    @patch('StudentProcess.get_students', return_value=[
        {"StudentID": "1", "Name": "John Doe"}
    ])
    @patch('StudentProcess.calculate_gpa', return_value=3.8)
    @patch('StudentProcess.get_scholarships', return_value=[
        {"ScholarshipID": "1", "Name": "Merit Scholarship", "GPARequirement": "3.5"},
        {"ScholarshipID": "2", "Name": "Excellence Award", "GPARequirement": "3.75"}
    ])
    def test_get_students_eligible_for_scholarships(self, mock_get_scholarships, mock_calculate_gpa, mock_get_students):
        eligible_students = get_students_eligible_for_scholarships()

        # Assert that only one student entry exists
        self.assertEqual(len(eligible_students), 1)  # One student entry

        # Verify the correct scholarships are combined in one entry
        self.assertIn("Merit Scholarship, Excellence Award", eligible_students[0]["Scholarships"])

    @patch('StudentProcess.calculate_gpa', return_value=3.6)
    @patch('StudentProcess.get_scholarships', return_value=[
        {"ScholarshipID": "1", "Name": "Merit Scholarship", "GPARequirement": "3.5"},
        {"ScholarshipID": "2", "Name": "Excellence Award", "GPARequirement": "3.75"},
    ])
    def test_multiple_scholarships_eligibility(self, mock_get_scholarships, mock_calculate_gpa):
        eligible_scholarships = check_scholarship_eligibility("1")
        self.assertEqual(len(eligible_scholarships), 1)  # Only Merit Scholarship applies


class TestDataIntegrity(unittest.TestCase):
    def setUp(self):
        # Mock data for integrity tests
        self.mock_grades = [
            {"StudentID": "1", "ClassID": "101", "Grade": "A", "Year": "2023", "Semester": "Fall"},
            {"StudentID": "2", "ClassID": "102", "Grade": "B", "Year": "2023", "Semester": "Spring"},
        ]
        self.mock_classes = [
            {"ClassID": "101", "ClassName": "Math", "Credits": "3", "InstructorID": "1"},
            {"ClassID": "102", "ClassName": "History", "Credits": "2", "InstructorID": "2"},
        ]
        self.mock_students = [
            {"StudentID": "1", "Name": "John Doe"},
            {"StudentID": "2", "Name": "Jane Smith"},
        ]

    @patch('StudentProcess.get_grades', return_value=[])
    def test_no_duplicate_entries_in_grades(self, mock_get_grades):
        # Adding the same class twice
        add_future_class("1", "101", "Fall", "2023")
        add_future_class("1", "101", "Fall", "2023")

        grades = mock_get_grades()
        student_grades = [g for g in grades if g["StudentID"] == "1" and g["ClassID"] == "101"]
        self.assertEqual(len(student_grades), 1)  # Should only have one entry

    @patch('StudentProcess.get_classes', return_value=[])
    def test_unique_class_id_in_classes(self, mock_get_classes):
        classes = mock_get_classes()
        class_ids = [c["ClassID"] for c in classes]
        self.assertEqual(len(class_ids), len(set(class_ids)), "Duplicate class IDs detected")

    @patch('StudentProcess.get_students', return_value=[])
    def test_unique_student_id_in_students(self, mock_get_students):
        students = mock_get_students()
        student_ids = [s["StudentID"] for s in students]
        self.assertEqual(len(student_ids), len(set(student_ids)), "Duplicate student IDs detected")

    @patch('StudentProcess.get_scholarships', return_value=[])
    def test_unique_scholarship_id_in_scholarships(self, mock_get_scholarships):
        scholarships = mock_get_scholarships()
        scholarship_ids = [s["ScholarshipID"] for s in scholarships]
        self.assertEqual(len(scholarship_ids), len(set(scholarship_ids)), "Duplicate scholarship IDs detected")

    @patch('StudentProcess.get_grades', return_value=[
        {"StudentID": "1", "ClassID": "999", "Grade": "A", "Year": "2023", "Semester": "Fall"},
    ])
    @patch('StudentProcess.get_classes', return_value=[])
    def test_invalid_class_id_in_grades(self, mock_get_classes, mock_get_grades):
        grades = mock_get_grades()
        classes = mock_get_classes()

        invalid_classes = [g for g in grades if g["ClassID"] not in [c["ClassID"] for c in classes]]
        self.assertTrue(len(invalid_classes) > 0, "No invalid class IDs detected")

    @patch('StudentProcess.get_grades', return_value=[
        {"StudentID": "999", "ClassID": "101", "Grade": "A", "Year": "2023", "Semester": "Fall"},
    ])
    @patch('StudentProcess.get_students', return_value=[])
    def test_invalid_student_id_in_grades(self, mock_get_students, mock_get_grades):
        grades = mock_get_grades()
        students = mock_get_students()

        invalid_students = [g for g in grades if g["StudentID"] not in [s["StudentID"] for s in students]]
        self.assertTrue(len(invalid_students) > 0, "No invalid student IDs detected")


if __name__ == "__main__":
    unittest.main()

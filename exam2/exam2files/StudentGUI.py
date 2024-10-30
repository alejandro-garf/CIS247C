# StudentGUI.py
#Alejandro Fonseca Exam 2

import tkinter as tk
from tkinter import ttk
import StudentProcess
import tkinter.messagebox as messagebox


class StudentManagementSystem:
    def __init__(self, tk_root):
        self.root = tk_root
        self.root.title("Student Management System")
        self.create_styles()
        self.setup_ui()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TLabel", padding=5, font=("Arial", 12), foreground='#333333')
        self.style.configure("TEntry", font=("Arial", 24))
        self.style.configure("Treeview", font=("Arial", 10), rowheight=25, background='#ffffff', foreground='#000000')
        self.style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#D3D3D3", foreground="black")
        self.style.configure("TNotebook.Tab", padding=[5, 5], focuscolor="none")
        self.style.configure("TButton", padding=10, font=("Arial", 12, "bold"), background="#007bff", foreground="white")
        self.style.configure("TCombobox", padding=5, font=("Arial", 12), fieldbackground="white", background="white", foreground="black")
        self.style.configure("Hover.TButton", background="#0056b3", foreground="white")
        self.style.map("TCombobox",
                       fieldbackground=[("readonly", "white"), ("!readonly", "white"), ("active", "lightblue")],
                       background=[("readonly", "white"), ("!readonly", "white"), ("active", "lightblue")],
                       selectbackground=[("readonly", "white"), ("!readonly", "white")],
                       selectforeground=[("readonly", "black"), ("!readonly", "black")])
        self.style.map("TButton", background=[("active", "#0056b3"), ("!disabled", "#007bff")])
        self.style.map("TNotebook.Tab", focuscolor=[("!focus", "#D3D3D3")])
        self.style.map("Treeview.Heading", background=[("active", "#D3D3D3"), ("pressed", "#D3D3D3")],
                       foreground=[("active", "black"), ("pressed", "black")])
        self.style.map('Treeview', background=[('selected', '#4CAF50'), ('!selected', '#f8f8f8')],
                       foreground=[('selected', 'white'), ('!selected', '#000000')])

    def setup_ui(self):
        self.main_frame = ttk.Frame(self.root, padding=(20, 20, 20, 20))
        self.main_frame.pack(fill='both', expand=True)
        self.create_notebook()
        self.populate_class_overview()

    def create_notebook(self):
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(pady=10, expand=True)

        # Creating frames for each tab
        self.frames = {
            "past_classes": ttk.Frame(self.notebook, width=500, height=400),
            "add_classes": ttk.Frame(self.notebook, width=500, height=400),
            "class_overview": ttk.Frame(self.notebook, width=500, height=400),
            "data_viewer": ttk.Frame(self.notebook, width=500, height=400)
        }

        # Add frames to notebook as tabs
        self.notebook.add(self.frames["class_overview"], text="Class Overview")
        self.notebook.add(self.frames["past_classes"], text="Past Classes")
        self.notebook.add(self.frames["add_classes"], text="Add Future Classes")
        self.notebook.add(self.frames["data_viewer"], text="Data Viewer")

        self.create_past_classes_tab()
        self.create_add_classes_tab()
        self.create_data_viewer_tab()

    def create_past_classes_tab(self):
        frame = self.frames["past_classes"]
        student_label = ttk.Label(frame, text="Enter Student ID:")
        student_label.pack(pady=10)

        self.student_entry = ttk.Entry(frame, width=30, font=("Arial", 16))
        self.student_entry.pack(pady=5)

        btn_view_past = ttk.Button(frame, text="View Past Classes", command=self.view_past_classes)
        btn_view_past.pack(pady=10)

        btn_gpa = ttk.Button(frame, text="Calculate GPA", command=self.calculate_gpa)
        btn_gpa.pack(pady=5)

        btn_scholarship = ttk.Button(frame, text="Check Scholarship Eligibility", command=self.check_scholarship)
        btn_scholarship.pack(pady=5)

        text_frame = ttk.Frame(frame)
        text_frame.pack(pady=25, padx=25, fill="both", expand=True)

        self.result_text = tk.Text(text_frame, wrap='word', width=60, height=15, font=("Arial", 10))
        self.result_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(text_frame, command=self.result_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=scrollbar.set)

    def create_add_classes_tab(self):
        frame = self.frames["add_classes"]
        add_class_label = ttk.Label(frame, text="Add Future Class for Student")
        add_class_label.pack(pady=10)

        add_student_label = ttk.Label(frame, text="Enter Student ID:")
        add_student_label.pack(pady=5)
        self.add_student_entry = ttk.Entry(frame, width=30, font=("Arial", 16))
        self.add_student_entry.pack(pady=5)

        add_class_id_label = ttk.Label(frame, text="Enter Class ID:")
        add_class_id_label.pack(pady=5)
        self.add_class_id_entry = ttk.Entry(frame, width=30, font=("Arial", 16))
        self.add_class_id_entry.pack(pady=5)

        semester_label = ttk.Label(frame, text="Select Semester:")
        semester_label.pack(pady=5)
        self.semester_combobox = ttk.Combobox(frame, values=["Fall", "Spring", "Summer"], state="readonly", font=("Arial", 12))
        self.semester_combobox.pack(pady=5)

        year_label = ttk.Label(frame, text="Select Year:")
        year_label.pack(pady=5)
        self.year_combobox = ttk.Combobox(frame, values=["2023", "2024", "2025"], state="readonly", font=("Arial", 12))
        self.year_combobox.pack(pady=5)

        btn_add_class = ttk.Button(frame, text="Add Class", command=self.add_future_class)
        btn_add_class.pack(pady=10)

        btn_profile = ttk.Button(frame, text="View Student Profile", command=self.get_student_profile)
        btn_profile.pack(pady=5)

        profile_text_frame = ttk.Frame(frame)
        profile_text_frame.pack(pady=10, fill="both", expand=True)

        self.result_profile_text = tk.Text(profile_text_frame, wrap='word', width=60, height=15, font=("Arial", 10))
        self.result_profile_text.pack(side="left", fill="both", expand=True)

        profile_scrollbar = ttk.Scrollbar(profile_text_frame, command=self.result_profile_text.yview)
        profile_scrollbar.pack(side="right", fill="y")
        self.result_profile_text.config(yscrollcommand=profile_scrollbar.set)

    def create_data_viewer_tab(self):
        frame = self.frames["data_viewer"]
        view_type_label = ttk.Label(frame, text="Select Data View:")
        view_type_label.pack(pady=10)

        view_options = ["Student Grades Report", "Classes with Instructors", "Students Eligible for Scholarships"]
        self.view_combobox = ttk.Combobox(frame, values=view_options, state="readonly", font=("Arial", 12))
        self.view_combobox.pack(pady=5)
        self.view_combobox.config(width=25)

        # Container for Treeview and Scrollbar
        container = ttk.Frame(frame)
        container.pack(pady=10, fill="both", expand=True)

        # Treeview for displaying data
        self.data_tree = ttk.Treeview(container, columns=("ID", "Name", "Details1", "Details2", "Details3"),
                                      show="headings")
        self.data_tree.pack(side="left", fill="both", expand=True)

        # Vertical scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.data_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.data_tree.config(yscrollcommand=scrollbar.set)

        # Set up Treeview headings and columns
        self.data_tree.heading("ID", text="ID")
        self.data_tree.heading("Name", text="Name")
        self.data_tree.heading("Details1", text="Details 1")
        self.data_tree.heading("Details2", text="Details 2")
        self.data_tree.heading("Details3", text="Details 3")

        self.data_tree.column("ID", width=150)
        self.data_tree.column("Name", width=150)
        self.data_tree.column("Details1", width=150)
        self.data_tree.column("Details2", width=150)
        self.data_tree.column("Details3", width=150)

        # Button to update view
        btn_update_view = ttk.Button(frame, text="Update View", command=self.populate_data_view)
        btn_update_view.pack(pady=10)

    def view_past_classes(self):
        student_id = self.student_entry.get()
        if not self.validate_student_id(student_id):
            return
        try:
            result = StudentProcess.get_student_past_classes(student_id)
            formatted_result = StudentProcess.format_past_classes(result)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Displaying past classes for Student ID: {student_id}\n\n{formatted_result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving data: {str(e)}")

    def calculate_gpa(self):
        student_id = self.student_entry.get()
        if not self.validate_student_id(student_id):
            return
        try:
            result = StudentProcess.calculate_gpa(student_id)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Calculating GPA for Student ID: {student_id}\n\nGPA: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving data: {str(e)}")

    def check_scholarship(self):
        student_id = self.student_entry.get()
        if not self.validate_student_id(student_id):
            return
        try:
            result = StudentProcess.check_scholarship_eligibility(student_id)
            formatted_result = StudentProcess.format_scholarships(result)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END,
                                    f"Scholarship Eligibility for Student ID: {student_id}\n\n{formatted_result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving data: {str(e)}")

    def add_future_class(self):
        student_id = self.add_student_entry.get()
        class_id = self.add_class_id_entry.get()
        semester = self.semester_combobox.get()
        year = self.year_combobox.get()

        if not (self.validate_student_id(student_id) and self.validate_class_id(class_id) and
                self.validate_combobox_value(self.semester_combobox) and self.validate_combobox_value(
                    self.year_combobox)):
            return
        try:
            result = StudentProcess.add_future_class(student_id, class_id, semester, year)
            self.result_profile_text.delete(1.0, tk.END)
            if result == "Success":
                self.result_profile_text.insert(tk.END, f"Adding class {class_id} for Student ID: {student_id} in"
                                                        f" {semester} {year}")
            elif result:
                self.result_profile_text.insert(tk.END, f"Error: {result}")
            else:
                self.result_profile_text.insert(tk.END, "Failed to add class")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving data: {str(e)}")

    def get_student_profile(self):
        student_id = self.add_student_entry.get()
        if not self.validate_student_id(student_id):
            return
        try:
            profile_data = StudentProcess.get_student_profile(student_id)
            formatted_profile = StudentProcess.format_student_profile(profile_data)
            self.result_profile_text.delete(1.0, tk.END)
            self.result_profile_text.insert(tk.END, formatted_profile)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving data: {str(e)}")

    def populate_class_overview(self):
        try:
            class_overview = StudentProcess.get_class_overview()
            columns = class_overview["columns"]
            data = class_overview["data"]

            container = ttk.Frame(self.frames["class_overview"])
            container.pack(fill='both', expand=True)

            scrollbar = ttk.Scrollbar(container, orient="vertical")

            self.class_tree = ttk.Treeview(container, columns=list(columns.keys()), show="headings",
                                           yscrollcommand=scrollbar.set)
            self.class_tree.pack(side="left", fill="both", expand=True)

            scrollbar.config(command=self.class_tree.yview)
            scrollbar.pack(side="right", fill="y")

            for col_key, col_header in columns.items():
                self.class_tree.heading(col_key, text=col_header)
                self.class_tree.column(col_key, width=100)

            self.populate_class_data(data)

        except Exception as e:
            fallback_columns = {
                "ClassID": "Class ID",
                "ClassName": "Class Name",
                "Credits": "Credits",
                "Instructor": "Instructor",
                "Semester": "Semester",
                "Year": "Year"
            }
            fallback_data = [
                {"ClassID": 201, "ClassName": "Advanced Algebra", "Credits": 5, "Instructor": "Dr. Ramanujan",
                 "Semester": "Spring", "Year": "2024"},
                {"ClassID": 202, "ClassName": "Renaissance Art", "Credits": 3, "Instructor": "Prof. Da Vinci",
                 "Semester": "Fall", "Year": "2023"},
                {"ClassID": 203, "ClassName": "Astrophysics", "Credits": 4, "Instructor": "Dr. Hawking",
                 "Semester": "Spring", "Year": "2024"},
                {"ClassID": 204, "ClassName": "Cybersecurity", "Credits": 4, "Instructor": "Prof. Lovelace",
                 "Semester": "Fall", "Year": "2023"},
                {"ClassID": 205, "ClassName": "Evolutionary Biology", "Credits": 4, "Instructor": "Prof. Darwin",
                 "Semester": "Spring", "Year": "2024"},
                {"ClassID": 206, "ClassName": "Quantum Mechanics", "Credits": 5, "Instructor": "Dr. Einstein",
                 "Semester": "Fall", "Year": "2023"},
                {"ClassID": 207, "ClassName": "Ethics in AI", "Credits": 3, "Instructor": "Prof. Turing",
                 "Semester": "Spring", "Year": "2024"},
                {"ClassID": 208, "ClassName": "Machine Learning", "Credits": 4, "Instructor": "Dr. Ng",
                 "Semester": "Fall", "Year": "2023"},
                {"ClassID": 209, "ClassName": "Organic Chemistry", "Credits": 4, "Instructor": "Prof. Curie",
                 "Semester": "Spring", "Year": "2024"},
                {"ClassID": 210, "ClassName": "Music Theory", "Credits": 2, "Instructor": "Prof. Bach",
                 "Semester": "Fall", "Year": "2023"},
            ]

            container = ttk.Frame(self.frames["class_overview"])
            container.pack(fill='both', expand=True)

            scrollbar = ttk.Scrollbar(container, orient="vertical")

            self.class_tree = ttk.Treeview(container, columns=list(fallback_columns.keys()), show="headings", yscrollcommand=scrollbar.set)
            self.class_tree.pack(side="left", fill="both", expand=True)

            scrollbar.config(command=self.class_tree.yview)
            scrollbar.pack(side="right", fill="y")

            for col_key, col_header in fallback_columns.items():
                self.class_tree.heading(col_key, text=col_header)
                self.class_tree.column(col_key, width=100)

            self.populate_class_data(fallback_data)

        self.class_tree.bind("<Double-1>", self.on_class_double_click)

    def populate_class_data(self, data):
        for row in self.class_tree.get_children():
            self.class_tree.delete(row)

        for item in data:
            values = [item[col] for col in self.class_tree["columns"]]
            self.class_tree.insert("", "end", values=values)

    # def populate_class_overview(self):
    #     self.class_tree = ttk.Treeview(self.frames["class_overview"], columns=("ClassID", "ClassName", "Credits", "Instructor", "Semester", "Year"), show="headings")
    #     self.class_tree.pack(pady=10, fill="both", expand=True)
    #
    #     for col in ["ClassID", "ClassName", "Credits", "Instructor", "Semester", "Year"]:
    #         self.class_tree.heading(col, text=col)
    #         self.class_tree.column(col, width=100)
    #
    #     self.populate_class_data()
    #
    # def populate_class_data(self):
    #     for row in self.class_tree.get_children():
    #         self.class_tree.delete(row)
    #
    #     try:
    #         data = StudentProcess.get_all_classes()
    #         if not data:
    #             data = [
    #                 {"ClassID": 201, "ClassName": "Advanced Algebra", "Credits": 5, "Instructor": "Dr. Ramanujan",
    #                  "Semester": "Spring", "Year": "2024"},
    #                 {"ClassID": 202, "ClassName": "Renaissance Art", "Credits": 3, "Instructor": "Prof. Da Vinci",
    #                  "Semester": "Fall", "Year": "2023"},
    #                 {"ClassID": 203, "ClassName": "Astrophysics", "Credits": 4, "Instructor": "Dr. Hawking",
    #                  "Semester": "Spring", "Year": "2024"},
    #                 {"ClassID": 204, "ClassName": "Cybersecurity", "Credits": 4, "Instructor": "Prof. Lovelace",
    #                  "Semester": "Fall", "Year": "2023"},
    #                 {"ClassID": 205, "ClassName": "Evolutionary Biology", "Credits": 4, "Instructor": "Prof. Darwin",
    #                  "Semester": "Spring", "Year": "2024"},
    #                 {"ClassID": 206, "ClassName": "Quantum Mechanics", "Credits": 5, "Instructor": "Dr. Einstein",
    #                  "Semester": "Fall", "Year": "2023"},
    #                 {"ClassID": 207, "ClassName": "Ethics in AI", "Credits": 3, "Instructor": "Prof. Turing",
    #                  "Semester": "Spring", "Year": "2024"},
    #                 {"ClassID": 208, "ClassName": "Machine Learning", "Credits": 4, "Instructor": "Dr. Ng",
    #                  "Semester": "Fall", "Year": "2023"},
    #                 {"ClassID": 209, "ClassName": "Organic Chemistry", "Credits": 4, "Instructor": "Prof. Curie",
    #                  "Semester": "Spring", "Year": "2024"},
    #                 {"ClassID": 210, "ClassName": "Music Theory", "Credits": 2, "Instructor": "Prof. Bach",
    #                  "Semester": "Fall", "Year": "2023"},
    #             ]
    #
    #         for item in data:
    #             self.class_tree.insert("", "end", values=(item["ClassID"], item["ClassName"], item["Credits"],
    #                                                       item["InstructorID"]))
    #     except Exception as e:
    #         messagebox.showerror("Error", f"An error occurred while retrieving data: {str(e)}")

    def populate_data_view(self):
        selected_view = self.view_combobox.get()
        if not self.validate_combobox_value(self.view_combobox):
            return

        for row in self.data_tree.get_children():
            self.data_tree.delete(row)

        try:
            if selected_view == "Student Grades Report":
                columns = ["StudentID", "Name", "ClassName", "Grade", "Year"]
                headers = ["Student ID", "Student Name", "Class Name", "Grade", "Year"]
                self.configure_treeview(columns, headers)
                data = StudentProcess.get_student_grades_report()
                if not data:
                    data = [
                        {"StudentID": 21, "Name": "Alice Wonderland", "ClassName": "Advanced Algebra", "Grade": "A",
                         "Year": "2024"},
                        {"StudentID": 22, "Name": "Bob Marley", "ClassName": "Renaissance Art", "Grade": "B+",
                         "Year": "2024"},
                        {"StudentID": 23, "Name": "Charlie Brown", "ClassName": "Astrophysics", "Grade": "A-",
                         "Year": "2024"},
                        {"StudentID": 24, "Name": "Diana Prince", "ClassName": "Cybersecurity", "Grade": "B",
                         "Year": "2023"},
                        {"StudentID": 25, "Name": "Edward Scissorhands", "ClassName": "Evolutionary Biology",
                         "Grade": "C+", "Year": "2024"},
                        {"StudentID": 26, "Name": "Fiona Apple", "ClassName": "Quantum Mechanics", "Grade": "A",
                         "Year": "2023"},
                        {"StudentID": 27, "Name": "Gordon Freeman", "ClassName": "Ethics in AI", "Grade": "A-",
                         "Year": "2024"},
                        {"StudentID": 28, "Name": "Harry Potter", "ClassName": "Machine Learning", "Grade": "B+",
                         "Year": "2023"},
                        {"StudentID": 29, "Name": "Isaac Newton", "ClassName": "Organic Chemistry", "Grade": "B",
                         "Year": "2023"},
                        {"StudentID": 30, "Name": "Jasmine Aladdin", "ClassName": "Music Theory", "Grade": "A",
                         "Year": "2023"},
                    ]

                for item in data:
                    self.data_tree.insert("", "end", values=(item.get("StudentID", ""), item.get("Name", ""),
                                                             item.get("ClassName", ""), item.get("Grade", ""),
                                                             item.get("Year", "")))
            elif selected_view == "Classes with Instructors":
                columns = ["ClassID", "ClassName", "Credits", "Instructor", "Department"]
                headers = ["Class ID", "Class Name", "Credits", "Instructor", "Department"]
                self.configure_treeview(columns, headers)
                data = StudentProcess.get_classes_with_instructors()
                if not data:
                    data = [
                        {"ClassID": 201, "ClassName": "Advanced Algebra", "Credits": 5, "Instructor": "Dr. Ramanujan",
                         "Department": "Mathematics"},
                        {"ClassID": 202, "ClassName": "Renaissance Art", "Credits": 3, "Instructor": "Prof. Da Vinci",
                         "Department": "Arts"},
                        {"ClassID": 203, "ClassName": "Astrophysics", "Credits": 4, "Instructor": "Dr. Hawking",
                         "Department": "Physics"},
                        {"ClassID": 204, "ClassName": "Cybersecurity", "Credits": 4, "Instructor": "Prof. Lovelace",
                         "Department": "Computer Science"},
                        {"ClassID": 205, "ClassName": "Evolutionary Biology", "Credits": 4,
                         "Instructor": "Prof. Darwin", "Department": "Biology"},
                        {"ClassID": 206, "ClassName": "Quantum Mechanics", "Credits": 5, "Instructor": "Dr. Einstein",
                         "Department": "Physics"},
                        {"ClassID": 207, "ClassName": "Ethics in AI", "Credits": 3, "Instructor": "Prof. Turing",
                         "Department": "Philosophy"},
                        {"ClassID": 208, "ClassName": "Machine Learning", "Credits": 4, "Instructor": "Dr. Ng",
                         "Department": "Computer Science"},
                        {"ClassID": 209, "ClassName": "Organic Chemistry", "Credits": 4, "Instructor": "Prof. Curie",
                         "Department": "Chemistry"},
                        {"ClassID": 210, "ClassName": "Music Theory", "Credits": 2, "Instructor": "Prof. Bach",
                         "Department": "Music"},
                    ]

                for item in data:
                    self.data_tree.insert("", "end", values=(item.get("ClassID", ""), item.get("ClassName", ""),
                                                             item.get("Credits", ""), item.get("Instructor", ""),
                                                             item.get("Department", "")))
            elif selected_view == "Students Eligible for Scholarships":
                columns = ["StudentID", "Name", "GPA", "Scholarship"]
                headers = ["Student ID", "Name", "GPA", "Scholarship"]
                self.configure_treeview(columns, headers)
                data = StudentProcess.get_students_eligible_for_scholarships()
                if not data:
                    data = [
                        {"StudentID": 21, "Name": "Alice Wonderland", "GPA": "3.9",
                         "ScholarshipName": "Academic Excellence", "Requirement": "3.75"},
                        {"StudentID": 22, "Name": "Bob Marley", "GPA": "3.5", "ScholarshipName": "Merit Scholarship",
                         "Requirement": "3.5"},
                        {"StudentID": 23, "Name": "Charlie Brown", "GPA": "3.8",
                         "ScholarshipName": "STEM Excellence Award", "Requirement": "3.8"},
                        {"StudentID": 24, "Name": "Diana Prince", "GPA": "3.4",
                         "ScholarshipName": "Arts Talent Scholarship", "Requirement": "3.4"},
                        {"StudentID": 25, "Name": "Edward Scissorhands", "GPA": "3.7",
                         "ScholarshipName": "Need-Based Scholarship", "Requirement": "2.5"},
                        {"StudentID": 26, "Name": "Fiona Apple", "GPA": "4.0", "ScholarshipName": "Academic Excellence",
                         "Requirement": "3.75"},
                        {"StudentID": 27, "Name": "Gordon Freeman", "GPA": "3.6",
                         "ScholarshipName": "Merit Scholarship", "Requirement": "3.5"},
                        {"StudentID": 28, "Name": "Harry Potter", "GPA": "3.9",
                         "ScholarshipName": "STEM Excellence Award", "Requirement": "3.8"},
                        {"StudentID": 29, "Name": "Isaac Newton", "GPA": "3.5",
                         "ScholarshipName": "Need-Based Scholarship", "Requirement": "2.5"},
                        {"StudentID": 30, "Name": "Jasmine Aladdin", "GPA": "3.7",
                         "ScholarshipName": "Academic Excellence", "Requirement": "3.75"},
                    ]

                for item in data:
                    self.data_tree.insert("", "end", values=(item.get("StudentID", ""), item.get("Name", ""),
                                                             item.get("GPA", ""), item.get("Scholarships", ""),
                                                             item.get("Requirement", "")))

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while retrieving data: {str(e)}")

    def configure_treeview(self, columns, headers):
        self.data_tree["columns"] = columns
        for col, header in zip(columns, headers):
            self.data_tree.heading(col, text=header)
            self.data_tree.column(col, width=150)

    def insert_data_into_treeview(self, data, columns):
        for item in data:
            values = [item.get(col, "") for col in columns]
            self.data_tree.insert("", "end", values=values)

    def on_class_double_click(self, event):
        selected_item = self.class_tree.selection()
        if selected_item:
            index = self.class_tree.index(selected_item[0])

            try:
                class_data = StudentProcess.get_class_overview()["data"][index]
                class_id = class_data["ClassID"]

                students_enrolled = [
                    s["Name"] for s in StudentProcess.get_students_enrolled_in_class(class_id)
                ]

                students_info = ", ".join(students_enrolled) if students_enrolled else "No students enrolled."

                detailed_info = f"""
                        Class ID: {class_id}
                        Class Name: {class_data['ClassName']}
                        Students Enrolled: {students_info}
                        """
                messagebox.showinfo("Class and Students Enrolled", detailed_info)
            except Exception as e:
                messagebox.showerror("Error", "Invalid")

    @staticmethod
    def validate_combobox_value(combobox):
        valid_values = combobox['values']
        selected_value = combobox.get()
        if selected_value not in valid_values:
            messagebox.showerror("Invalid Selection", "Please select a valid value.")
            return False
        return True

    @staticmethod
    def validate_student_id(student_id):
        if not student_id.isdigit():
            messagebox.showerror("Invalid Input", "Student ID must be a number.")
            return False
        return True

    @staticmethod
    def validate_class_id(class_id):
        if not class_id.isdigit():
            messagebox.showerror("Invalid Input", "Class ID must be a number.")
            return False
        return True


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()

from model import Student, Course
from typing import List
from prettytable import PrettyTable
from tabulate import tabulate


class SystemManager:
    def __init__(self) -> None:
        self.students: List[Student] = []
        self.courses: List[Course] = []

    def add_student(self, name: str) -> None:
        self.students.append(Student(name))

    def remove_student(self, student_id: int) -> None:
        self.students = [
            student for student in self.students if student.student_id != student_id
        ]

    def add_course(self, name: str) -> None:
        self.courses.append(Course(name))

    def remove_course(self, course_id: int) -> None:
        self.courses = [
            course for course in self.courses if course.course_id != course_id
        ]

    def enroll_student_in_courses(self, student_id: int, course_ids: List[int]):
        student = next((s for s in self.students if s.student_id == student_id), None)
        for id in course_ids:
            course = next((c for c in self.courses if c.course_id == id), None)

            if student and course:
                student.enroll_in(course)
                course.enroll_students(student)

    def search_courses(self, search_name: str) -> str:
        return ", ".join(
            [
                course.name
                for course in self.courses
                if search_name.lower() in course.name.lower()
            ]
        )

    def record_grade(self, student_id: int, course_id: int, grade: int) -> None:
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)

        if student and course:
            student.add_grade(course, grade)

    def get_all_students(self) -> List[Student]:
        students = []
        for student in self.students:
            students.append(student)

        return students

    def get_all_courses(self) -> List[Course]:
        courses = []
        for course in self.courses:
            courses.append(course)

        return courses

    def get_all_info(self):
        student_table = [[s.student_id, s.name] for s in self.students]
        print("STUDENTS")
        print(tabulate(student_table, headers=["ID", "Name"], tablefmt="grid"))
        print()

        course_table = [[c.name, len(c.enrolled_students)] for c in self.courses]
        print("COURSES")
        print(
            tabulate(
                course_table,
                headers=["Course Name", "Enrolled Students"],
                tablefmt="grid",
            )
        )

    def get_student_x_info(self, s_id: int):
        student = next((s for s in self.students if s.student_id == s_id), None)
        if not student:
            print(f"No student found with ID {s_id}")
            return

        if student.grades:
            course_table = [[course, grade] for course, grade in student.grades.items()]
        else:
            course_table = [["None", "N/A"]]

        print(f"STUDENT {student.student_id} INFO")
        info_table = [["ID", student.student_id], ["Name", student.name]]
        print(tabulate(info_table, tablefmt="grid"))
        print("\nEnrolled Courses and Grades:")
        print(tabulate(course_table, headers=["Course Name", "Grade"], tablefmt="grid"))

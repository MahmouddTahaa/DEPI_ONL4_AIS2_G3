from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .course import Course


class Student:
    _student_id = 1

    def __init__(self, name: str) -> None:
        self.student_id = Student._student_id
        Student._student_id += 1
        self.name = name
        self.grades = {}
        self.enrolled_courses = []

    def add_grade(self, course: Course, grade) -> None:
        self.grades[course.name] = grade

    def enroll_in(self, course: Course) -> None:
        self.enrolled_courses.append(course.name)

    def __str__(self) -> str:
        return f"Student ID: {self.student_id}, Name: {self.name}"

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .student import Student


class Course:
    _course_id = 1

    def __init__(self, name: str) -> None:
        self.course_id = Course._course_id
        Course._course_id += 1
        self.name = name
        self.enrolled_students = []

    def enroll_students(self, student: Student):
        self.enrolled_students.append(student)

    def __str__(self) -> str:
        return f"Course ID: {self.course_id}, Name: {self.name}"

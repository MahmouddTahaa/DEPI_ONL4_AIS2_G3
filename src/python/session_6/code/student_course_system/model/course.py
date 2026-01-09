# from system_manager import *
#
from .student import Student


class Course:
    """A class to represent a course in the student-course management system."""

    _id_counter = 1

    def __init__(self, name: str) -> None:
        self.course_id = Course._id_counter
        Course._id_counter += 1
        self.name = name
        self.enrolled_students = []

    def __str__(self) -> str:
        return f"course ID : {self.course_id}, Name : {self.name}, Enrolled: {len(self.enrolled_students)}"

    def __repr__(self) -> str:
        return f"course ID : {self.course_id}, Name : {self.name}, Enrolled: {len(self.enrolled_students)}"

    def enroll_student(self, student: Student) -> None:
        """
        Enrolls a student in the course.

        Args:
            student (Student): The student to enroll.

        Returns:
            None
        """
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"student enrolled successfully in {self.name}")
        else:
            print(f"student is already enrolled in {self.name}")

    def remove_student(self, student: Student) -> None:
        """
        Removes a student from the course.

        Args:
            student (Student): The student to remove.

        Returns:
            None
        """
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"student removed from {self.name}")
        else:
            print(f"student is not enrolled in {self.name}")

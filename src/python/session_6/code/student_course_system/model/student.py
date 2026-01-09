class Student:
    """A class to represent a student in the student-course management system."""

    _id_counter = 1

    def __init__(self, name: str) -> None:
        self.student_id = Student._id_counter
        Student._id_counter += 1
        self.name = name
        self.grades = {}
        self.enrolled_courses = []

    def __str__(self) -> str:
        return (
            f"Student ID: {self.student_id}, Name: {self.name}, Grades: {(self.grades)}"
        )

    def add_grade(self, course_id: int, grade: str) -> None:
        """
        Adds or updates the grade for a specific course.

        Args:
            course_id (int): The ID of the course.
            grade (str): The grade to be assigned.

        Returns:
            None
        """
        self.grades[course_id] = grade

    def enroll_in_course(self, course) -> None:
        """
        Enrolls the student in a given course.

        Args:
            course (Course): The course to enroll in.

        Returns:
            None
        """
        self.enrolled_courses.append(course)

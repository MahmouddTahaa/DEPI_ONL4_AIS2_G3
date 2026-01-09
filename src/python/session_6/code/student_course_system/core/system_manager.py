from model.course import Course
from model.student import Student


class SystemManager:
    """
    Manages the student-course system, including adding/removing students and courses,
    enrolling students in courses, searching for courses, and recording grades."""

    def __init__(self) -> None:
        # id is the key, object is the value
        self.students = {}
        self.courses = {}

    def add_student(self, name: str) -> int:
        """
        Adds a new student to the system.

        Args:
            name (str): Name of the student

        Returns:
            int: The ID of the newly added student
        """
        student = Student(name)
        self.students[student.student_id] = student
        print("Student added successfully.")
        return student.student_id

    def remove_student(self, student_id: int) -> None:
        """
        Removes a student from the system.

        Args:
            student_id (int): ID of the student to be removed

        Returns:
            None
        """
        if student_id in self.students:
            student = self.students[student_id]
            if not student.enrolled_courses:
                del self.students[student_id]
                print("Student removed successfully.")
            else:
                print("Student has enrolled courses. Cannot remove.")
        else:
            print("Invalid student ID.")

    def add_course(self, name: str) -> int:
        """
        Adds a new course to the system.

        Args:
            name (str): Name of the course

        Returns:
            int: The ID of the newly added course
        """
        course = Course(name)
        self.courses[course.course_id] = course
        print("Course added successfully.")
        return course.course_id

    def remove_course(self, course_id: int) -> None:
        """
        Removes a course from the system.

        Args:
            course_id (int): ID of the course to be removed

        Returns:
            None
        """
        if course_id in self.courses:
            course = self.courses[course_id]
            if not course.enrolled_students:
                del self.courses[course_id]
                print("Course removed successfully.")
            else:
                print("Course has enrolled students. Cannot remove.")
        else:
            print("Invalid course ID.")

    def enroll_course(self, student_id: int, course_id: int) -> None:
        """
        Enrolls a student in a course.

        Args:
            student_id (int): ID of the student to be enrolled
            course_id (int): ID of the course to be enrolled in

        Returns:
            None
        """
        # First few check if the student and course exist
        if student_id in self.students and course_id in self.courses:
            # Then we retrieve the student and course objects from the dictionaries we declared in __init__ of SystemManager class
            student = self.students[student_id]
            course = self.courses[course_id]
            # Here we check if the student is already enrolled in the course
            if course.name not in student.enrolled_courses:
                student.enroll_in_course(course.name)
                course.enroll_student(student.name)
                print("Student enrolled in course successfully.")
            else:
                print("Student is already enrolled in the course.")
        else:
            print("Invalid student or course ID.")

    def search_courses(self, search_name: str) -> list:
        """
        Searches for courses by name.

        Args:
            search_name (str): Name of the course to search for

        Returns:
            list: List of course names that match the search criteria
        """
        result = []
        for course in self.courses.values():
            if search_name.lower() == course.name.lower():
                result.append(course.name)
        return result

    def record_grade(self, student_id: int, course_id: int, grade: str) -> None:
        """
        Records a grade for a student in a specific course.

        Args:
            student_id (int): ID of the student
            course_id (int): ID of the course
            grade (float): Grade to be recorded

        Returns:
            None
        """
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.add_grade(course.name, grade)
            print("Grade recorded successfully.")
        else:
            print("Invalid student or course ID.")

    def get_all_students(self):
        """
        Returns a list of all students in the system.

        Returns:
            list: List of Student objects
        """
        return list(self.students.values())

    def get_all_courses(self):
        """
        Returns a list of all courses in the system.

        Returns:
            list: List of Course objects
        """
        return list(self.courses.values())

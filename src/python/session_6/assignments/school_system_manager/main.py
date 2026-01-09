from core import SystemManager


def main():
    sys_man = SystemManager()

    sys_man.add_student("James")
    sys_man.add_student("Jacob")
    sys_man.add_student("Joshua")

    sys_man.add_course("Physics")
    sys_man.add_course("Geology")
    sys_man.add_course("History")

    sys_man.enroll_student_in_courses(1, [1, 2, 3])
    sys_man.enroll_student_in_courses(2, [1, 3])
    sys_man.enroll_student_in_courses(3, [1])

    sys_man.record_grade(1, 1, 60)
    sys_man.record_grade(1, 2, 40)
    sys_man.record_grade(1, 3, 30)

    sys_man.record_grade(2, 1, 30)
    sys_man.record_grade(2, 3, 90)

    sys_man.record_grade(3, 1, 100)

    students = sys_man.get_all_students()
    courses = sys_man.get_all_courses()

    sys_man.get_all_info()

    print()

    sys_man.get_student_x_info(1)


if __name__ == "__main__":
    main()

print("Hello World")
class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student_id, name, age, email):
        """Add a new student to the system"""
        student = {
            'student_id': student_id,
            'name': name,
            'age': age,
            'email': email
        }
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def remove_student(self, student_id):
        """Remove a student from the system"""
        for student in self.students:
            if student['student_id'] == student_id:
                self.students.remove(student)
                print(f"Student {student_id} removed successfully!")
                return
        print(f"Student {student_id} not found!")

    def add_course(self, course_code, name, instructor, credits):
        """Add a new course to the system"""
        course = {
            'course_code': course_code,
            'name': name,
            'instructor': instructor,
            'credits': credits
        }
        self.courses.append(course)
        print(f"Course {name} added successfully!")

    def remove_course(self, course_code):
        """Remove a course from the system"""
        for course in self.courses:
            if course['course_code'] == course_code:
                self.courses.remove(course)
                print(f"Course {course_code} removed successfully!")
                return
        print(f"Course {course_code} not found!")

    def enroll_student(self, student_id, course_code):
        """Enroll a student in a course"""
        student_exists = any(s['student_id'] == student_id for s in self.students)
        course_exists = any(c['course_code'] == course_code for c in self.courses)

        if not student_exists:
            print(f"Student {student_id} not found!")
            return
        if not course_exists:
            print(f"Course {course_code} not found!")
            return

        enrollment = {
            'student_id': student_id,
            'course_code': course_code,
            'enrollment_date': datetime.datetime.now().strftime("%Y-%m-%d")
        }
        self.enrollments.append(enrollment)
        print(f"Student {student_id} enrolled in course {course_code} successfully!")

    def get_student_courses(self, student_id):
        """Get all courses a student is enrolled in"""
        enrolled_courses = []
        for enrollment in self.enrollments:
            if enrollment['student_id'] == student_id:
                course_code = enrollment['course_code']
                course = next((c for c in self.courses if c['course_code'] == course_code), None)
                if course:
                    enrolled_courses.append(course)
        return enrolled_courses

    def get_course_students(self, course_code):
        """Get all students enrolled in a course"""
        enrolled_students = []
        for enrollment in self.enrollments:
            if enrollment['course_code'] == course_code:
                student_id = enrollment['student_id']
                student = next((s for s in self.students if s['student_id'] == student_id), None)
                if student:
                    enrolled_students.append(student)
        return enrolled_students

    def display_student_info(self, student_id):
        """Display information about a specific student"""
        student = next((s for s in self.students if s['student_id'] == student_id), None)
        if student:
            print("\nStudent Information:")
            print(f"ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Email: {student['email']}")
            print("Enrolled Courses:")
            for course in self.get_student_courses(student_id):
                print(f"- {course['name']} ({course['course_code']})")
        else:
            print(f"Student {student_id} not found!")

    def display_course_info(self, course_code):
        """Display information about a specific course"""
        course = next((c for c in self.courses if c['course_code'] == course_code), None)
        if course:
            print("\nCourse Information:")
            print(f"Code: {course['course_code']}")
            print(f"Name: {course['name']}")
            print(f"Instructor: {course['instructor']}")
            print(f"Credits: {course['credits']}")
            print("Enrolled Students:")
            for student in self.get_course_students(course_code):
                print(f"- {student['name']} ({student['student_id']})")
        else:
            print(f"Course {course_code} not found!")

import datetime

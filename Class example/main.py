from _class import Student

student = Student(
    name="Akash R Chandran",
    place="Kollam",
    age=25
)
student.display_student_details()
print("="*20)
student.set_age(21)
# student.get_age()
student.display_student_details()
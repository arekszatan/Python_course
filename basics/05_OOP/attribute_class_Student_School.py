import random

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.school_name = None
        self.field_of_study = None

    def print_info(self):
        print(self.name, self.surname, self.age, self.city, self.school_name, self.field_of_study)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.students_list = []
        self.fields_of_study = ["IT", "Math", "Robotics"]

    def add_student(self, student):
        if isinstance(student, Student):
            self.students_list.append(student)
            student.school_name = self.name
            student.field_of_study = random.choice(self.fields_of_study)

    def print_school_info(self):
        print("School name: ", self.name, " City: ", self.city)
        print("Students: ")
        for el in self.students_list:
            el.print_info()

student1 = Student("Kasia", "Lis", 20, "Waw")
student1.school_name = "Tech School 1"
student1.country = "Poland"
student1.print_info()
print(student1.country)

student2 = Student("Adam", "Kowalski", 21, "Waw")

school = School("Tech School", "Krk")
school.add_student(student1)
school.add_student(student2)
print(" ")
school.print_school_info()
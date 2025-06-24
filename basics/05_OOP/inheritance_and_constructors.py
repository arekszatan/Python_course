
class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print("Person constructor!")

    def print_person_data(self):
        print("Person.print_person_data() ", self.name, self.surname, self.city)


person1 = Person("Ola", "Kowalska", "Krk")
person1.print_person_data()


class Employee(Person):
    def __init__(self, name, surname, city, company_name, salary):
        Person.__init__(self, name, surname, city)
        self.company_name = company_name
        self.salary = salary

        print("Employee constructor!")

    def print_employee_data(self):
        print("Employee.print_employee_data() ", self.name,
              self.surname, self.company_name, self.salary)

print(" ")
employee1 = Employee("Kasia", "Kot", "Waw", "Tech Ltd", 10000)
employee1.print_person_data()
employee1.print_employee_data()


class Manager(Employee):
    def __init__(self, name, surname, city, company_name, salary, department):
        Employee.__init__(self, name, surname, city, company_name, salary)
        self.department = department
        print("Manager constructor!")

    def hire_employee(self):
        print("Hire employee!")

    def print_manager_data(self):
        print("Manager data: ", self.name, self.surname, self.department)

print(" ")
manager1 = Manager("Ania", "X", "Waw", "Tech 2 Ltd", 15000, "IT")
manager1.print_person_data()
manager1.print_employee_data()
manager1.print_manager_data()
manager1.hire_employee()
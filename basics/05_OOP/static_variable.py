
class Employee:
    """Employee class describing company employee"""
    # static variable for all objects based no Employee
    num_employees = 0
    employees_list = []

    def __init__(self, name):
        """Constructor for employee class"""
        """
        linia 1
        linia 2
        """
        self.name = name

        Employee.num_employees += 1
        print(self.name, "num_employees: ", Employee.num_employees)

        Employee.employees_list.append(self)

    def print_all_employees(self):
        for el in Employee.employees_list:
            print(el.name)

employee1 = Employee("Ola")
employee2 = Employee("Kasia")
employee3 = Employee("Adam")
employee4 = Employee("Karol")

print("Employee.num_employees: ", Employee.num_employees)
print(" ")
employee1.print_all_employees()

help(Employee)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)

print("name attr in Employee: ",hasattr(employee1, "name"))
print("name attr in Employee: ",hasattr(employee1, "city"))
employee1.city = "Krk"
print("name attr in Employee: ",hasattr(employee1, "city") )

setattr(employee1, "name", "Kasia")
print("employee1.name: ", getattr(employee1, "name"))
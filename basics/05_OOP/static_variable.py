
class Employee:
    num_employees = 0
    employees_list = []

    def __init__(self, name):
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
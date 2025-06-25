import os, pickle

script_dir = os.path.dirname(__file__)


class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def __str__(self):
        return f"Name: {self.name}, surname: {self.surname}, city: {self.city}"

    def print_something(self):
        print("Something printed!")

person1 = Person("Ola", "Kowalska", "Krk")
person2 = Person("Adam", "Kot", "Gd")
person3 = Person("Kasia", "Kowalska", "Waw")

fh = open(script_dir + "/people.dat", "wb")
pickle.dump(person1, fh)
pickle.dump(person2, fh)
pickle.dump(person3, fh)
person_list = [person1, person2, person3]
pickle.dump(person_list, fh)
fh.close()

fh = open(script_dir + "/people.dat", "rb")
person1_info = pickle.load(fh)
person2_info = pickle.load(fh)
person3_info = pickle.load(fh)
person_list_info = pickle.load(fh)
print(person1_info)
print(person2_info)
print(person3_info)
print(person_list_info)

for person in person_list_info:
    person.print_something()
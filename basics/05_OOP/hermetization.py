
class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.__gears = 5

    def __get_gears_info_str(self):
        return f'Gears number ' + str(self.__gears)

    def print_info(self):
        print(self.brand, self.name,
              self.__get_gears_info_str())


vehicle1 = Vehicle("Dodge", "Charger")
# print(vehicle1.__gears) # AttributeError
# vehicle1.__get_gears_info_str() # AttributeError
vehicle1.print_info()
# print(vehicle1._Vehicle__gears) # niezalecane


class Car(Vehicle):
    def __init__(self, brand, name):
        Vehicle.__init__(self, brand, name)
        # print(self.__gears) # AttributeError
        # print(self.__get_gears_info_str()) # AttributeError


car1 = Car("Ford", "Mustang")
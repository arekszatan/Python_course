
class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.top_speed = 10
        self.num_wheels = 4

    def print_vehicle_info(self):
        print("print_vehicle_info ", self.brand, self.name,
              self.top_speed, self.num_wheels)


vehicle1 = Vehicle("Vehicle", "basic")
vehicle1.print_vehicle_info()

class Car(Vehicle):
    def print_car_info(self):
        self.top_speed = 230
        print("print_car_info ", self.brand, self.name,
              self.top_speed, self.num_wheels)

    def print_vehicle_info(self):
        print("Car.print_vehicle_info ", self.brand, self.name,
              self.top_speed, self.num_wheels)

    def print_num_wheels(self):
        print("Car.numWheels: ", self.num_wheels)

car1 = Car("Ford", "Mustang")
car1.print_car_info()
car1.print_vehicle_info()
car1.print_num_wheels()


class SuperCar(Car):
    def reach_speed_300(self):
        self.top_speed = 301
        print("Super car reach 300!")

super_car_1 = SuperCar("Opel", "Astra")
super_car_1.reach_speed_300()
super_car_1.print_vehicle_info()
super_car_1.print_num_wheels()
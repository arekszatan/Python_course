
class Car:
    def __init__(self, brand, name, color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1
        self.top_speed = 0
        self.set_top_speed(230)
        self.print_info()

    def print_info(self):
        print(self.brand, self.name, self.color, self.mileage, self.year, self.top_speed)

    def set_top_speed(self, top_speed):
        self.top_speed = top_speed

mustang = Car("Ford", "Mustang", "Red", "2025")
# print(dir(Car))
mustang.mileage = 100
mustang.print_info()

charger = Car("Dodge", "Charger", "Red", "2025")

# print(charger.top_speed)
for d in dir(mustang):
    if d.startswith("__"):
        continue
    print(d)

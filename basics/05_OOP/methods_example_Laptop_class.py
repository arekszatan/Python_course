
class Laptop:
    def __init__(self, cpu, ram = 4096, gpu = "AMD", price = 2000):
        self.cpu = None
        self.ram = None
        self.gpu = gpu
        self.price = price
        self.set_cpu(cpu)
        self.set_ram(ram)


    def set_cpu(self, cpu):
        if cpu.lower() == "amd" or cpu.lower() == "intel" or cpu.lower() == "arm":
            self.cpu = cpu
        else:
            self.cpu = "unknown"

    def set_ram(self, ram):
        if type(ram) == int and ram >= 2048:
            self.ram = ram
        else:
            self.ram = "unknown"
            print("Ram must be an integer or larger equal 2048!")

    def print_data(self):
        print(self.cpu, self.ram, self.gpu, self.price)

laptop1 = Laptop("Intel", 1024)
laptop1.print_data()

laptop2 = Laptop("AMD", 32000)
laptop2.print_data()
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

    def start_engine(self):
        print("Engine has started")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def load_cargo(self):
        print("Truck is being loaded with cargo")


class Electric(Car):
    def __init__(self, make, model, year, num_doors, battery_capacity):
        super().__init__(make, model, year, num_doors)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        print("Battery is being charged")

if __name__ == "__main__":
    v = Vehicle("Toyota", "Camry", 2022)
    v.display_info()
    v.start_engine()

    c = Car("Honda", "Accord", 2021, 4)
    c.display_info()
    c.start_engine()

    t = Truck("Ford", "F150", 2020, 2000)
    t.display_info()
    t.start_engine()

    e = Electric("Tesla", "Model S", 2023, 4, 25)
    e.display_info()
    e.start_engine()
    e.charge_battery()

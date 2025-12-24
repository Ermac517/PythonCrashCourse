from car import Car as Car

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 200  # Default range for other battery sizes

        print(f"This car can go approximately {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        self.battery.describe_battery()

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model} Electric"
        return long_name.title()

my_electric_car = ElectricCar('tesla', 'model s', 2020)
print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()
my_electric_car.update_odometer(15_000)
my_electric_car.read_odometer()
my_electric_car.battery.get_range()
from car import Car as Car

my_new_car = Car('ford', 'mustang', 2021)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(5000)
my_new_car.read_odometer()
my_new_car.increment_odometer(150)
my_new_car.read_odometer()
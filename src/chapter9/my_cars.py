from car import Car as Car
from electric_car import ElectricCar as ElectricCar

my_mustang = Car('ford', 'mustang', 2021)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2022)
print(my_leaf.get_descriptive_name())
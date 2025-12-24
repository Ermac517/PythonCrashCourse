class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        return f"{self.name} is now sitting."
    
    def roll_over(self):
        return f"{self.name} rolled over!"

    def bark(self):
        return "Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."

my_dog = Dog("Buddy", 3)
print(my_dog.get_info())
print(my_dog.sit())
print(my_dog.roll_over())
print(my_dog.bark())

your_dog = Dog("Max", 5)
print(your_dog.get_info())
print(your_dog.sit())
print(your_dog.roll_over())
print(your_dog.bark())
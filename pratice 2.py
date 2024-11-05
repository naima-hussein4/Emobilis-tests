#Class and Object Creation
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Call the display_info() method
my_car.display_info()
#Encapsulation
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

# Create an instance of the BankAccount class
account = BankAccount(1000)

# Deposit and withdraw money
account.deposit(500)
account.withdraw(200)
#Inheritance
class Animal:
    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

# Create an instance of the Dog class
my_dog = Dog()

# Use inherited methods and the new method
my_dog.eat()
my_dog.sleep()
my_dog.bark()
my_dog
#Polymorphism
class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof")

def animal_sound(animal):
    animal.make_sound()

# Create instances of Cat and Dog
cat = Cat()
dog = Dog()

# Call the animal_sound function with different animal objects
animal_sound(cat)
animal_sound(dog)
#Constructor Overloading
class Rectangle:
    def __init__(self, side=None, length=None, width=None):
        if side:
            self.length = side
            self.width = side
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width

# Create a square and a rectangle
square = Rectangle(5)
rectangle = Rectangle(length=4, width=6)

print(square.area())
print(rectangle.area())
#Method Overriding
class Employee:
    def calculate_salary(self):
        print("Calculating salary...")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary for manager...")
        # Specific salary calculation for manager

# Create instances of Employee and Manager
employee = Employee()
manager = Manager()

employee.calculate_salary()
manager.calculate_salary()
#Composition
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()

    def stop_car(self):
        self.engine.stop()

# Create a car instance and use its methods
car = Car()
car.start_car()
car.stop_car()
#Static Methods and Attributes
class Calculator:
    count = 0

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Use the static method and check the count
result = Calculator.add(5, 3)
print(result)
print(Calculator.count)
#Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Create two vectors
v1 = Vector(2, 3)
v2 = Vector(4, 1)

# Add the vectors using the + operator
v3 = v1 + v2

print(v3)  # Output: Vector(6, 4)
#Abstract Classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Create instances of Circle and Square
circle = Circle(5)
square = Square(4)

# Calculate and print areas
print(circle.area())
print(square.area())

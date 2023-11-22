# Class and Object:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Create an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Access attributes and call methods
print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.bark()



# Encapsulation:

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # _balance is a protected attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.withdraw(500)
print("Balance:", account.get_balance())

#Inheritance:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.speak())
print(my_cat.speak())

#Polymorphism:

def animal_sound(animal):
    return animal.speak()

my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(animal_sound(my_dog))
print(animal_sound(my_cat))

#Abstraction:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

square = Square(5)
circle = Circle(3)

print("Square Area:", square.area())
print("Circle Area:", circle.area())

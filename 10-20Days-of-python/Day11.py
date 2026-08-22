class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # Private attribute

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:  # Validation
            self.__age = age
        else:
            print("Invalid age")

# Usage
student = Student("Anita", 20)
print("Age:", student.get_age())  # Accessing age with getter
student.set_age(21)  # Modifying age with setter
print("Updated Age:", student.get_age())

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,balance):
        if balance>0:
           self.__balance=balance
user_1=BankAccount(2000)
print("Balance:" ,user_1.get_balance())
user_1.set_balance(1500)
print("Updated balance:" ,user_1.get_balance())

#MethodOverloading
class Calculator:
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c

    def multiply(self):
        if self.c is None:
            print(self.a * self.b)
        else:
            print(self.a * self.b * self.c)


mul = Calculator(5, 6, 7)
mul.multiply()

mul = Calculator(5, 10)
mul.multiply()

class Calculator:
    def multiply(self, *numbers):
        result = 1

        for num in numbers:
            result *= num

        return result


calc = Calculator()

print(calc.multiply(5, 6))
print(calc.multiply(5, 6, 7))

#Overriding
class Vehicle:

    def start(self):
        print("Vehicle started")

class Car(Vehicle):

    def start(self):
        print("Car starts with key")

class Bike(Vehicle):

    def start(self):
        print("Bike → Bike starts with button")

car = Car()
bike = Bike()

car.start()
bike.start()

from abc import ABC,abstractmethod
class Empolyee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Empolyee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate
manager = Manager(40, 500)

print(manager.calculate_salary())

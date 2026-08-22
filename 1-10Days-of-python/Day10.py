#Inheritance
class Vehicle:

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):

    def drive(self):
        print("Car is driving")

class Bike(Vehicle):

    def ride(self):
        print("Bike is riding")

car = Car()
bike = Bike()

car.start()
car.stop()
car.drive()


class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog=Dog()
dog.eat()

#2
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
s=Student("Rohith",20,"AIML")
s.display()

#3
class Animal:
    def sound(self):
        print("Animal makes a sound")

class dog(Animal):
    def sound(self):
        print("Dog is braking")

Dog=dog()
Dog.sound()

#4
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size

    def manage(self):
        print(f"Managing a team of {self.team_size} people")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def code(self):
        print(f"Coding in {self.programming_language}")

manager = Manager("Roy", 80000, 10)
developer = Developer("Rahul", 60000, "Python")

manager.display()
manager.manage()

developer.display()
developer.code()

#Polymorphism
class Animal:
    def sound(self):
        print("OH it's making sound")

class dog(Animal):
    def sound(self):
        print("dog is barking")

class cat(Animal):
    def sound(self):
        print("Meow")

a=dog()
b=cat()
a.sound()
b.sound()

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

class dog:
    def sound(self):
        print("Bow")
class cat:
    def sound(self):
        print("Meow")
class cow:
    def sound(self):
        print("Boo")

def make_sound(animal):
    animal.sound()

a=dog()
b=cat()
c=cow()
make_sound(a)
make_sound(b)
make_sound(c)

class UPI:
    def pay(self):
        print("Payed through UPI.")

class Creaditcard:
    def pay(self):
        print("Payed through Creaditcard")

class Cash:
    def pay(self):
        print("Payed through cash")

def procces_payment(payment):
    payment.pay()

a=UPI()
b=Creaditcard()
c=Cash()

procces_payment(a)
procces_payment(b)
procces_payment(c)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * self.radius * self.radius)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of rectangle: {self.length * self.width}")


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Area of square: {self.side * self.side}")


def calculate_area(shape):
    shape.area()


a = Circle(5)
b = Rectangle(10, 20)
c = Square(4)

calculate_area(a)
calculate_area(b)
calculate_area(c)

# Final last 5 coding questions
class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance

    def deposite(self,amount):
        self.__balance+=amount
        print(f"Your bank balance is {self.__balance} ")

    def withdraw(self,amount):
        if self.__balance> amount:
            self.__balance-=amount
            print(f"You withdraw {amount} and your balance is {self.__balance}")


a=BankAccount(12345,1000)
a.deposite(100)
a.withdraw(200)

#abstraction
class Phone :
    def __init__(self,contact,picture):
        self.contact=contact
        self.picture=picture
    def call_contact(self):
        print(f"There are {self.contact} contacts in your phone")

    def take_picture(self):
        print(f"There are {self.picture} pictures in your phone")

a=Phone(500,1000)
a.call_contact()
a.take_picture()

#Inheritance
class Vehical:
    def start(self):
        print("Vehical started")

class car(Vehical):
    def stop(self):
        print("Car is stopped")

class bike(Vehical):
    def stop(self):
        print("Bike is stopped")

a=bike()
b=car()
a.start()

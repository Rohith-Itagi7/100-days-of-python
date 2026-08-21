#Encapulation
class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        print(f"This is your balance {self.__balance}")

a=bankaccount(1000)
a.get_balance()
           
class student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        print(f"Name: {self.__name}")
    def get_age(self):
        print(f"Age: {self.__age}")

person1=student("Rohith",22)
print(person1.__name)
person1.get_name()
person1.get_age()

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposite(self,amount):
        if amount>0 :
            self.__balance+=amount

    def  withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount

    def display_balance(self):
        print(f"Your balance is {self.__balance}")

a=BankAccount(1000)
a.deposite(500)
a.withdraw(300)
a.display_balance()

#Abstraction
from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(animal):
    def sound(self):
        print("Dog barks")

d=Dog()
d.sound()

from abc import ABC,abstractclass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * self.radius * self.radius)

class rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)

ci=circle(5)
rec=rectangle(5,10)
ci.area()
rec.area()


from abc import ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass
class car(Vehical):
    def start(self):
        print("Car starts with a key")
class bike(Vehical):
    def start(self):
        print("Bike start with a self-start")

a=car()
b=bike()

a.start()
b.start()


class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def delete_user(self, user):
        print(f"Admin {self.username} deleted user {user}")

admin = Admin("karnataka_admin")
admin.login()  # Inherited from User
admin.delete_user("user_102")  # Admin-specific method

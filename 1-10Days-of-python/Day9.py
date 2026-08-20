# Create a Class:

# Write a class Mobile with attributes brand and price.
# Create two objects of the class and display their attributes using a method.
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand #Attributes
        self.price=price

    def buy(self): #Methods
        print(f"This phone brand is {self.brand} and price is {self.price}")

#created multiple objects
my_phone=Mobile("Vivo","699")
my_phone_2=Mobile("Redme","999")
my_phone.buy()
my_phone_2.buy()

# Method Definition:

# Define a class Student with attributes name and marks.
# Write a method display_info() that prints the student's name and marks.
# Create multiple objects of the Student class and call the method on each.

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f"Student name:{self.name}\nStudent marks : {self.marks}")

Roll_no_1=student("Rohith",75)
Roll_no_2=student("shivu",80)

Roll_no_1.display_info()
Roll_no_2.display_info()

# Default Parameters:

# Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
# Write a method that displays the details of each employee.
# Create multiple Employee objects with different values for name and designation, and test the default salary behavior.

class Empolyee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary
    def display(self):
        print(f"Details:\n{self.name}\n{self.designation}\n{self.salary}")

a=Empolyee("Rohith","Phd")
b=Empolyee("Sunil","MCA")
Empolyee.display(a)
b.display()

Create a Student class and create 2 objects from it.
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return f"Your name {self.name} and age is {self.age}"
a=Student("Rohith",99)
b=Student("Manu",47)

print(a.name)
print(b.name)

class Book:
    pass

book1 = Book()
book2 = Book()

print(type(book1))
print(type(book2))

class Mobile:
    def __init__(self,brand,price):
        self.brand=brand #Attributes
        self.price=price

    def buy(self): #Methods
        print(f"This phone brand is {self.brand} and price is {self.price}")

#created multiple objects
my_phone=Mobile("Vivo","699")
my_phone_2=Mobile("Redme","999")
#checking is object belongs to class
print(isinstance(my_phone,Mobile))
print(isinstance(my_phone_2,Mobile))

# Create a Rectangle class with:
# length
# width
# Create methods:
# area()
# perimeter()

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(f" Area : {self.length * self.width}")

    def perimeter(self):
        print(f" Perimeter : {2 * self.length * self.width}")
a=Rectangle(10,20)
a.area()
a.perimeter()


#Class with three objects
class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department

    def display(self):
        print(f"Details: {self.name} {self.salary} {self.department}")
emp1=Employee("Rohith",45000,"AIML")
emp2=Employee("Girish",50000," CSE")
emp3=Employee("Virat",60000,"Data-science")
emp1.display()
emp2.display()
emp3.display()

class counter:
    def __init__(self,count):
        self.count=count

    def increment(self):
        self.count+=1

c=counter(0)
c.increment()
c.increment()
print(c.count)


class bankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposite(self,amt):
        self.balance+=amt
        print(f"Deposited {amt}. New balance: {self.balance}")
    def withdraw(self,amt):
        if self.balance>=amt:
            self.balance-=amt
            print(f"Withdrew {amt}. New balance: {self.balance}")
        else:
            print("Invalid balance")  

a=bankAccount(1000)
a.deposite(500)
a.withdraw(200)


#instance variable and class variable
class Car:
    wheels=4
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"Your car brand is {self.brand} and price is {self.price} and {self.wheels} wheels")

car1 = Car("Toyota", 2000000)
car2 = Car("BMW", 5000000)
car3 = Car("Audi", 4000000)

car1.display()
car2.display()
car3.display()

class Mobile:
    category = "Electronics"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f"Your phone brand is {self.brand} and price is {self.price} and category is {self.category}")

Mobile.category="Communication"

a=Mobile("Vivo",799)
b=Mobile("Realme",688)
a.display()
b.display()

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


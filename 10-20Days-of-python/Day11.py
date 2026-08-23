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

#   Simple Calculator
print("Simple Calculator")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

def add(a,b):
    return a+b
user_input=int(input("Enter your choice (1-5):"))

if user_input in {1,2,3}:
    a=float(input("Enter the frist number:"))
    b=float(input("Enter the second number:"))
if user_input==1:
    print(f"Result: {a} + {b} ={add(a,b)}")
elif user_input==2:
    a=float(input("Enter the frist number:"))
    b=float(input("Enter the second number:"))
    c=a-b
    print(f"{a} - {b} ={c}")
elif user_input==3:
    a=input("Enter the frist number:")
    b=input("Enter the second number:")
    c=a*b
    print(f"{a} * {b} ={c}")
elif user_input==4:
    a=input("Enter the frist number:")
    b=input("Enter the second number:")
    c=a/b
    print(f"{a} / {b} ={c}")

if user_input==5:
    print("Exiting the calculator.Goodbye!")


class Grocerystore:
    def __init__(self):
        self.cart={}

    def add_item(self,item,price):
        self.cart[item]=price

    def remove_item(self,item):
        if item in self.cart:
            del self.cart[item]
        else:
            return "No such item found"
    def total_price(self):
        total=sum(self.cart.values())
        print(f"The total price {total}")

    def display(self):
        print("\n--- Grocery Store ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View total price")
        print("4. Exit")

store=Grocerystore()

while True:
    store.display()
    choice=int(input("Enter the choice:"))

    if choice==1:
        item=input("Enter the item:")
        price=int(input("Enter the price"))
        store.add_item(item, price)
    elif choice==2:
        item=input("Enter the item ")
        store.remove_item(item)
    elif choice==3:
        store.total_price()
    else:
        print("Thank you")
        break

#Educational system
class education:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
        
    def display_student(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


def display():
        print("1.Add Student")
        print("2.Display student")
        print("3.Exit")
    

Student=[]
while True:

    display()
    choice=int(input("Enter the Creadentials: "))
    if choice==1:
        name=input("Enter the student name:")
        age=input("Enter the student age:")
        course=input("Enter the student opted course:")
        student=education(name,age,course)
        Student.append(student)
        print("Student details Added succesfully..")
    if choice==2:
        if len(Student)==0:
            print("No student detials found..")
        else:
            for student in Student:
                student.display_student()
    if choice==3:
        print("Thank you.")
        break

        


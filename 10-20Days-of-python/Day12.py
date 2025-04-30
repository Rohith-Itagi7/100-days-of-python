# Namespaces:local v/s Global scope
#local scope
def greet():
    walking=2
    print(walking)
""" here walking is defined inside the greet function so the walking variable can  be used just inside the function."""
print(walking)

def greet():
    def hello():
        print(hello())
"""Even here the function hello is inside the greet function hence it is also local scope """
print(hello())

#global scope
walking=2

def greet():
    print(walking)
""" here variable is defined outside the function so we can acces anywhere hence it is called global scope"""
print(walking)

#Program for chechking wheather the number is prime or not
def is_prime(num):
    if num==2:
        return True
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

age=5
body_parts=["Heart","Kidney","Brain"],
if age>0:
    my_variable=[body_parts][0]
print(my_variable)
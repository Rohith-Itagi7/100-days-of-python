def decorator(func):
    def wrapper():
        print("Namskara")
        func()
        print("Ok")
    return wrapper
@decorator
def into():
    print("hahaha")

into()

#decorators with arguments and loging
def show_result(func):
    def wrapper(a,b):
        print(f"This function '{func.__name__ }'is called")
        func(a,b)
    return wrapper
    
@show_result
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

add(5,10)
sub(10,5)

#logging
def log_function_call(func):
    def wrapper():
        print(f"This function '{func.__name__ }'is called")
        func()
    return wrapper()

@log_function_call
def add():
    print("Add")

import time

def time_taken(func):
    def wrapper():
        print("Time started")
        start=time.time()
        func()
        end=time.time()
        execution_time = end - start
        print(f"Task completed time taken : {execution_time}")
    return wrapper

@time_taken
def long_task():
    time.sleep(2)
    
    
long_task()

def adds(func):
    def wrapper(a,b):
        print("===")
        func(a,b)
        print("===")
    return wrapper
def arrow(func):
    def wrapper(a,b):
        print(">>>")
        func(a,b)
    return wrapper

@arrow
@adds

def add(a,b):
    print(a+b)

add(10,5)

def allow_only(func):
    def wrapper(name):
        if name=="Admin":
            func(name)
        else:
            print("Acces diened ")
    return wrapper

@allow_only
def view_data(name):
    print(f"Name:{name}")

view_data("Admin")

temps_c = [25, 30, 35, 40]
def calc(c):
    return (c * 9/5) + 32
final=map(calc,temps_c)
print(list(final))

cities = ["Bengaluru", "Mysuru", "Mandya", "Hubballi", "Ballari", "Hassan"]

def start_with(city):
    return city.startswith("M")
final=filter(start_with,cities)
print(list(final))

from functools import reduce
scores = [45, 67, 89, 34, 76, 90]

total= reduce(lambda a,b: a if a>b else b,scores) 
print(total)

marks = [35, 50, 66, 20, 88, 75]

total=map(lambda x: x+10,marks)
print(list(total))

total=filter(lambda x:x>50,marks)
print(list(total))

total=reduce(lambda x,y:x+y,marks)
print(total)

#Def function -Fuction is defined using a def keyword and a function ame with parameters and arguments
def datting(boy,girl):
    print(f"{boy} is dating {girl}")

datting("Rohith","Rohini")#positional arguments

def datting(girl,boy):
    print(f"{boy} is dating {girl}")

datting(boy="Rohith",girl="Rohini")#key word arguments

def datting(boy,girl="Anushka"): #defualt parameter just  taking as a default value
    print(f"{boy} is dating {girl}")

datting("Rohith")

#return keyword helps to return the function value were we can use that function value wherever we want
def my_car(a,b):
    return a+b 

c=my_car(1,3)
print(c)


x=15 #Global Variable
def datting(boy,girl):
    print(f"{boy} is dating {girl}")
    x=10 #Local Variable
    print(x)

datting("Rohith","Rohini")
print(x)

# Coding challenges 
def greet():
    print("Welcome to the Pannel")

greet()

def greet_user(user):
    print(f"Hello {user} Welcome to the Pannel")

greet_user("Rohith")
greet_user("Rohini")

def add_numbers(a, b):
    print(a+b)

add_numbers(2,4)
add_numbers(5,6)

# Reason why we use Variable length arguments  
def func(name,age):
    return f"Hello {name} your age is {age}"

func("Rohith") #func() missing 1 required positional argu

# *args it gives output in place of tuple
def func(*a):
    return f"Hello {a} "
c=func("Rohith","Rohini","Masa")
print(c)

# kwargs
def my_fuc(**a):
    for key,values in a.items():
        print(f"{key} :{values}")
my_fuc(name="Rohith",age=22, habit="Footbal")

#lambda function
dobule= lambda x:x**2
print(dobule(2))

#recursion
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

result=factorial(4)
print(result)

#nested Def functions
def calculations(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    def mul():
        return a*b
    return add(), sub() ,mul()
print(calculations(10,3))

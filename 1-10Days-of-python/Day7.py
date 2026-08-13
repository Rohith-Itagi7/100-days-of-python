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

result=factorial(5)
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

#print 1 to n
def print_num(n):
    if n == 1:
        return [1]

    return print_num(n - 1) + [n]

print(print_num(5))

#print n to 1
def my_num(n):
    if n==1:
        return [1]
    return [n]+ my_num(n-1)
print(my_num(5))

#Sum of n numbers 
def my_sum(n):
    if n==1:
        return 1
    return n + my_sum(n-1)

print(my_sum(5))

factorial
def pow_num(base,exp):
    if exp==1:
        return base
    return base*pow_num(base,exp-1)

print(pow_num(3,4))


def count_digits(n):
    if n<10:
        return 1
    return 1+ count_digits(n//10)

print(count_digits(12345))

def reverse_string(n):
    if len(n)==1:
        return n

    return reverse_string(n[1:])+n[0]
print(reverse_string("Roy"))

def palin(n):
    if len(n)==1:
        return 
    return n+ palin(n[0])==n[]

print(palin("madam"))

lambda functions

add=lambda x,y:x+y
print(add(5,10))

students = [
    ("Roy", 90),
    ("John", 70),
    ("Alice", 85)
]
so=sorted(students,key=lambda x:x[1])
print(so)

nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))

print(result)

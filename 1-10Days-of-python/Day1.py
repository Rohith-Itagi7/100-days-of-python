print("Rohith Itagi")
print("Namskara")

#Variables
a=10 #int
b=20
print(a+b)

Name="Rohith" #String
print(Name)

A=22.0   #Float
print(A)

is_strong=True  #boolean
print(is_strong)

#Type checking
a=10
print(type(a))

#Type Converstion
x=100
s="22"
f=22.0
print(int(s)+x)
print(int(f)+x)


a=10
b=5
user=input("Enter the operation:+.-,*,/")
def add():
    return a+b
def sub():
    return a-b
def mul():
    return a*b
def div():
    return a/b
if user=="+":
    print(add())
elif user=="-":
    print(sub())
elif user=="*":
    print(mul())
else:
    print(div())

#Swapping two numbers
a=10
b=15

a,b=b,a
print(a)
print(b)

# Using third variable
c=a
a=b
b=c
print(a)
print(b)

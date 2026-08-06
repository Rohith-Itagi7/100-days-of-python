#String Manipulation
age=int(input("What is you age:"))
print("Hello " + "Rohith " + "your age is " + str(age) )

name="Rohith Itagi"
age=21
full_details= name + " " + str(age)
print(full_details)

name=input("Enter the boy name: ")
name_1=input("Enter the girl name: ")
print(f"{name}   loves {name_1}")

name="Rohith\n"* 10
print(name)

# String methods
Your_city="Hello world!"
print(Your_city.strip("a"))
print(Your_city.upper())
print(Your_city.lower())
print(Your_city.replace("world","Boss"))

#Accessing element
print(len(Your_city))
print(Your_city[2])
print(Your_city[0:5])
print(Your_city[::2])

#Home-work
user_input=input("Enter your name :")

print(user_input.upper())
print(user_input.lower())
print(user_input.replace(" " , "_"))
print(len(user_input))
print(len((user_input).strip()))

a=20
b=30
print(a>b and b<a)
print(a>b or b>a)
print(a>b and not b<a)
age=int(input("Enter your age:"))
if age==18:
    print("Your adult")
elif age>=18:
    print("Full adult")
else:
    print("Your a Child")

name="Rohith"
print("t" in name)
print("r" not in name)

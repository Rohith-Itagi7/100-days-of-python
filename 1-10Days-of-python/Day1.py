# Write a program that uses print statements to print the following recipe into the Output console.
# The text to print is already there, you just need to make it into code.

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#String Manipulation
print("Hello world!\nHello world!\nHello world!")
print("hello"+ " "+ "Angela")
print("hello "+ input("what is your name:?") + "!")

#Python Variable
name="Hi How are you"
print(name)

user_name="Welcome"
length=len(user_name)
print(length)

# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. 
# You are only allowed to use variables to solve this exercise.
glass2 = "milk"
glass1 = "juice"

temp=glass1
glass1=glass2
glass2=temp

print(glass1)
print(glass2)

# Create a greeting for your program.
# Ask the user for the city that they grew up in and store it in a variable.
# Ask the user for the name of a pet and store it in a variable.
# Combine the name of their city and pet and show them their band name.

print("Band Name Generator Project")
user=input("What's the name of the city you grew up in?\n")
user_pet=input("What's your pet's name?\n")
print(f"Your band name could be {user} {user_pet}")
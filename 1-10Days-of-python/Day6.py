# Function to greet a user
def greet(name):
    print(f"Hello, {name}! Welcome to Python programming.")

greet("Alice")

# Program to count from 1 to 5 using while loop
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1

# Define a function to print a welcome message
def welcome():
    print("Welcome to Python programming!")

welcome()
welcome()
welcome()

# Call the function multiple times using a loop
for i in range(3):
    welcome()
    
# Call the function multiple times using a while loop
count = 0
while count < 3:
    welcome()
    count += 1

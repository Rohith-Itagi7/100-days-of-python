"""Here i have debuged the range function to include the 20"""
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

"""I have debugged the erorr of randint function to access the elements from list where randint includes inclusive of end number but range function doesnt support inclusive of end number"""
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])

"""Frist time i tried using try except( exception handling method)here we will be knowing it may throw any error so it's helps us to overcome from error by using try,except."""
try:
    age = int(input("How old are you?"))
except ValueError:
        print("Invalid thing!.Use numerical for execution")
        age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")

#Even we can debug our errors through using print() built i function.

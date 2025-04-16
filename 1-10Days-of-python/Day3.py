#if-else statement
height=int(input("Enter your height:"))

if height >=120:
    print("You can play any games")
else:
    print("Sorry! Your are too short")

#using Modulo
user=int(input("Enter any number"))
if user%2==0:
    print("Yup its even number")
else:
    print("Oh its odd")

#Nested statements(if and elif)
height=int(input("Enter your height:"))

if height >=120:
    print("You can play any games")
    age=int(input("Enter your age:"))
    if age>=18:
       print("You have to pay $5")
    elif age<=12:
        print("You are not eligible")
    elif age<=18:
        print("You have pay $9")
else:
    print("Sorry! Your are too short")
# BMI Calculator with Interpretations
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi<18.5:
    print("Underweight")
elif 18.5<= bmi <25:
    print("normal weight")
elif bmi>=25:
    print("Overweight")

#Multiple If
height=int(input("Enter your height:"))
bill=0
if height >=120:
    print("You can play any games")
    age=int(input("Enter your age:"))
    if age>=18:
       bill=5
       print("You have to pay $5")
    elif age<=12:
        bill=7
        print("You have to pay $7")
    elif age<=18:
        bill=9
        print("You have pay $9")
    want_photos=input("If you want photo y/s?").lower()
    if want_photos=="y":
        bill+=3

    print(f"Your total height checking cost is {bill}")

else:
    print("Sorry! Your are too short")

#Pizza Order program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size=="S":
   bill=15
elif size=="M":
    bill=20
elif size=="L":
    bill=25
else:
    print("You have entered wrong input")
if pepperoni == "Y":
    if size=="S":
      bill += 2
    else:
      bill+=3
if extra_cheese=="Y":
  bill+=1
print(f"Your final bill is: ${bill}.")
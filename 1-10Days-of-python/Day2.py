#Datatypes

#String
print("Hello")
print("123"+"455")

#bolean
print(True)
print(False)

# float
print(3.555)

#integer
print(455+233)

#largenumbers
print(123_4556_789)

# Type Checking
print(type(123))
print(type("123"))
print(type(123.55))
print(type(True))

# Type converstion
print("Number of letters in your name: " + str(len(input("Enter your name"))))
print(int("154"))
print(str(123))
print((int(3.14)))

#Mathematical Operations
print(5-2)
print(3*3)
print(6/3)
print(6//3)
print(3**2)
#PEMDAS
print(3 *( 3 + 3 )/ 3 - 3)
print(3 * 3 + 3 / 3 - 3)

# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
# This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
height = 1.65 
weight = 84
bmi =weight/height**2
print(bmi)

#Rounding a number
print(bmi)
print(int())
print(round(bmi))
print(round(bmi,2))
#Number Manipulation
age=0

age+=1
age-=1
age*=1
#Usage of formatted  string
score=0
name="Virat"
is_running=True

print(f"Hey yor name is {name} and your score is {score} is always {is_running}")

#Tip calculator project
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill + total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(final_amount)

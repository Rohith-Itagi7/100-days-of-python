Time=20
if Time==20:
    print("It's time up")

age=int(input("Enter the age :"))
if age<11:
   print("You are young")
elif age==18:
    print("adult")
if age>18:
   print("You have reached adult age")
else:
   print("your still young")
   if age>11 and age<18:
      print("What's up still you wanna grow")

#Breakfast timing
time=int(input("Enter the time:"))

if time==8:
   print("Breakfast")
elif time==1:
   print("Lunch")
elif time==8:
   print("Dinner")
else:
   print("It's not a meal time.")

#Person eligible for library membership
age=int(input("Enter the age:"))

if age>18:
   print("You got the student membership.")
elif age<60:
   print("You got a senior citizen relationship")
else:
   print("You got a regular membership")


# while loop
i=0
while i<=5:
   i+=1
   print(i)

i=0
while i<=10:
   print(f"{i}")
   i+=1
   if i==5:
      break

i=0
while i<=10:
   i+=1
   if i==5:
      continue
   print(f"{ i }")

pin = ""
i=0
correct_pin = "1234"
while pin != correct_pin and i<=3:
    pin = input("Enter your PIN: ")
    i+=1
    if pin != correct_pin:
        print("Incorrect PIN. Try again.")
print("PIN accepted. You can proceed.")

#Homework
i=0
while i<=10:
   print(f"{i}")
   i+=1

i=1
while i<=20:
   while i%2==0:
      i+=1
      continue
   else:
      print(f"{i}")
      i+=1

bus_seat=8

is_always=True

while is_always and bus_seat>=0:
   book=input("Do you want to book:'Y/N'").lower()
   if book=="y":
      bus_seat-=1
      print(f"{bus_seat}")
   else:
      print('Thankyou for visting.All seat booked')
      break
i=10
while i>=1:
   print(f"{i}")
   i-=1
   if i==0:
      print("Happy new year")

#for loop
for i in range(1,11):
   print(f"3*{i}={3*i}")

text="Hello"
vowels = "aeiouAEIOU"
count=0
for i in text:
   if i in vowels:
      count+=1
print("Number of vowels:",count)

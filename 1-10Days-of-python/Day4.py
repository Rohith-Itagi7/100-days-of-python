import random

random_integer = random.randint(1, 10)
print(random_integer)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# Understanding the Offset and Appending Items to Lists

states_of_india=["Karnataka","Goa","MP","UP","HP","WB"]
print(states_of_india[-1])
print(states_of_india[1])
states_of_india[0]="Delhi"
states_of_india.append("Kerala")
states_of_india.extend(["GJ"])

print(states_of_india)
#Working with nested list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

#program
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_num=random.choice(friends)
print(random_num)

random_index=random.randint(0,4)
print(friends[random_index])

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

str_length=len(states_of_america)
print(states_of_america[str_length -1])

#final project
running_on=True
options = ("rock", "paper", "scissors")
while running_on :
   user_choice = None
   computer_choice = random.choice(options)
   if  user_choice not in options:
    user_choice = input("What do you choose?(rock,paper,scissors):")
   if user_choice==computer_choice:
      print("You win")
   elif user_choice=="rock" and computer_choice=="paper":
      print("You win")
   elif user_choice=="scissors" and computer_choice=="paper":
      print("You win")
   elif user_choice=="scissors" and computer_choice=="rock":
      print("You win")
   else:
    print("You loose")
    play_again=input("Do want to play again? y/n").lower()
    if not play_again=="y":
        running_on=False

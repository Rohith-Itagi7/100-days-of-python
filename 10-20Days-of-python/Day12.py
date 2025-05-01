# Namespaces:local v/s Global scope
#local scope
def greet():
    walking=2
    print(walking)
""" here walking is defined inside the greet function so the walking variable can  be used just inside the function."""
print(walking)

def greet():
    def hello():
        print(hello())
"""Even here the function hello is inside the greet function hence it is also local scope """
print(hello())

#global scope
walking=2

def greet():
    print(walking)
""" here variable is defined outside the function so we can acces anywhere hence it is called global scope"""
print(walking)

#Program for chechking wheather the number is prime or not
def is_prime(num):
    if num==2:
        return True
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
#NO Block Spaces
age=5
body_parts=["Heart","Kidney","Brain"]
if age>0:
    """In  if,while,for loop we can create the local variable and we can acces even after outside function."""
    my_variable=body_parts[0]
print(my_variable)

def hello():
    if age>0:
        my_variable=body_parts[0]

print(my_variable)

"""Global variable is useful for defining the constant """

#Modifying the global variable
count=0

def my_function():
    global count
    while count<=0:
        count+=1
        print(f"Inside function:{count}")

my_function()
print(f"Outside function:{count}")

#Number Guessing game
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")




game()


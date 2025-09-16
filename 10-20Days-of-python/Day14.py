from game_data import data
import random
from art import logo,vs

def interface(account):
     answer_name=account["name"]
     answer_dep=account["description"]
     answer_place=account["country"]
     return f"{answer_name} a {answer_dep} from {answer_place} "

def check_answer(guess,a_follower,b_follower):
    if a_follower>b_follower:
        return guess=="a"
    else:
        return guess=="b"
print(logo)
score=0
should_continue=True
user_b=random.choice(data)
while should_continue:
    user_a=user_b
    user_b=random.choice(data)
    if user_a==user_b:
       user_b=random.choice(data)
    #Here I have reused th function by calling diffrent argument
    print(f"Compare A:{interface(user_a)}")
    print(vs)
    print(f"Against B:{interface(user_b)}")
    user_guess=input("who has more followers? Type 'A' or 'B':").lower()
    a_follower_count=user_a["follower_count"]
    b_follower_count=user_b["follower_count"]
    is_correct=check_answer(user_guess,a_follower_count,b_follower_count)
    #Here I learnt if is_correct is true it execute if or it skips and prints else
    if is_correct:
       score+=1
       print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")

        should_continue=False

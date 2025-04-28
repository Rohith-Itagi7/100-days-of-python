# beginner - Hangman
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over=True
correct_word=[]
while  game_over:

    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
           display += letter
           correct_word.append(guess)
        elif letter in correct_word:
            display+=letter
        else:
           display += "_"

    print(display)
    if "_" not in display:
        print("you won")
        game_over=False
    else:
       display+="_"
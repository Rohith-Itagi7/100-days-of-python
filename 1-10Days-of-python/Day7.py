# beginner - Hangman
import random
list=["baboon","aadvark","camel"]
word_list=random.choice(list)

placeholder=""
word_len=len(word_list)
for position in range(word_len):
    placeholder+="_"
print(placeholder)

def life_in_weeks(age):
    years=90-age
    left_weeks=years*52

    print(f"You have {left_weeks} weeks")

life_in_weeks(56)

# positional Argument
def greet(name,location):
    print(f"Hello {name}")
    print(f"I am from {location}")

greet("Rohith","Davangere")

#Keyword Argument
def greet_homies(name,location):
    print(f"Hello {name}")
    print(f"I am from {location}")

greet_homies(location="Dharwad",name="Rohan")

#Program
def calculate_love_score(name1,name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")

# Caesar Chiper step_1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_txt,shift_amt):
    cipher_txt=""
    for letter in original_txt:
        shifted_position=alphabet.index(letter)+ shift_amt
        shifted_position %=len(alphabet)
        cipher_txt +=alphabet[shifted_position]

        print(cipher_txt)

encrypt(original_txt="text",shift_amt="shift")

#part_2
def caesar(original_text, shift_amount,direction):
    cipher_text = ""
    
    for letter in original_text:
        if direction=="decode":
           shift_amount*=-1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {direction}d result: {cipher_text}")


caesar(original_text=text, shift_amount=shift,encode_or_decode=direction)

#part3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

user=True
while user:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

import random
from HangmanWord import word_bank
from Hangmangrapics import logo
from Hangmangrapics import graphic
lives=6



choosen_word=random.choice(word_bank)
#print(choosen_word)
print(logo)
placeholder=""
word_length=len(choosen_word)
for position in range (word_length):
    placeholder+='_'
print(placeholder)

correct_letters=[]
game_over=False
while not game_over:
    guess=input("enter the letter:").lower()
    
    if guess  in correct_letters:
        print("Already guessed dont lose a life")

    '''for letter in choosen_word:
    if letter==guess:
        print("right")
    else:
        print("wrong")'''

    display=""

    for letter in choosen_word:
        if letter==guess:
            display+=guess
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'
    
    if guess not in choosen_word:
        lives-=1
        print(f"Guessed word {guess} is wrong you lose a life ")
        if lives==0:
            print("You Lose!!!")
            print(choosen_word)
            
            game_over=True

    print(display)
    if "_" not in display:
        game_over=True
        print("You Win!!!")
        print(choosen_word)
        break

    print(graphic[lives])
    print(f"lives left:{lives}")
    
from ART import Art
from Game_Data import Data
import random
print(Art)

Tv_Show1 = ""
Tv_Show2 = ""
Rate1 = 0
Rate2 = 0
score = 0

def format_data():
    global Tv_Show1
    global  Tv_Show2
    global Rate1
    global Rate2
    rand1 = random.choice(Data)
    rand2 = random.choice(Data)
    Tv_Show1 = rand1['Series_Name']
    Rate1 = rand1['Rate']
    Tv_Show2 = rand2['Series_Name']
    Rate2 = rand2['Rate']




def compare():
    format_data()
    A = Tv_Show1
    B = Tv_Show2
    global score
    choice = input(f"\n\nWhich Tv_show's Rate is Higher, Choose between A OR B: {A} VS. {B}\n")
    if choice == 'A' and Rate1 >= Rate2:
        print(f"congratolation, You Win!, {Tv_Show1}:{Rate1} VS. {Tv_Show2}:{Rate2}\n")
        score +=1
        print(f"Your Score: {score} \n")
    elif choice == 'A' and Rate1 <= Rate2:
        print(f"Sorry, Better Luck Next Time, {Tv_Show1}:{Rate1} VS. {Tv_Show2}:{Rate2}\n")
        print(f"Your Score: {score} \n")
    elif choice == 'B' and Rate2 >= Rate1:
        print(f"congratolation, You Win!, {Tv_Show1}:{Rate1} VS. {Tv_Show2}:{Rate2}\n")
        score += 1
        print(f"Your Score: {score} \n")
    elif choice == 'B' and Rate2 <= Rate1:
        print(f"Sorry, Better Luck Next Time, {Tv_Show1}:{Rate1} VS. {Tv_Show2}:{Rate2}\n")
        print(f"Your Score: {score} \n")




def game_func():
    game = input("\n\nType Y to play the game\n")
    start = True
    if game == 'Y':
        while start:
            compare()
            continuo = input("Type Y to continuo the game, Type N to stop\n")
            if continuo == 'Y':
                start = True
            elif continuo == 'N':
                start = False



game_func()
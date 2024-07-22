# Dice Roll

import random
anwser = random.randint(1,6)
repeat = True

while repeat:
    user_input = input("Select a number to Guess [1 , 6] : ")
    print("You rolled",anwser)
    if user_input == anwser:
        print("You won!")
    else:
        print("You Lost")
    print("Wanna Contiue? Yes / No")
    repeat = "Yes" in input()






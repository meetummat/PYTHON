# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import random

def game(): 
    print("You are playing a game..")
    score = random.randint(1, 61) # it will return random number from 1 to 60.

    # fetch the highscore
    with open("File_Input_Output_Py/File_Question_Py/game.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
             
    print(f"Your score : {score}")
    if score > hiscore or hiscore == "":
        # write highscore to the file.
        with open("File_Input_Output_Py/File_Question_Py/game.txt", "w") as f:
            f.write(str(score)) # write funcion only takes string.
    return score 

game()
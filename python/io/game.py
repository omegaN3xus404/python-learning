import random
def game():
    print("you are playing a game")
    score=random.randint(1,50)

    with open("game.txt","r")as f:
        highscore=f.read()
        if highscore!="":
            highscore=int(highscore)
        else:
            highscore=0

    print(f"your score is {score}")

    
    if(score>highscore):
            with open("game.txt","w") as f:
                f.write(str(score))

    return score


game()





    


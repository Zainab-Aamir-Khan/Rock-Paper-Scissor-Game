# Rock Paper Scissors
#start the game now

import random 
#rock wins over scissors
#scissors win over paper
#paper wins over rock 
print("Welcome To The Rock Paper Scissor Game!!!!!")

guess = ["rock", "paper", "scissors"]

while True:
    userInput = input("enter your choice: ")

    choice = random.choice(guess)
    print("you chose ", userInput)
    print("computer chose ", choice)

    if userInput == choice:
        print("It's a Tie!!!!")
    elif userInput == "rock" and userInput == "scissors":
        print("You won!!")
    elif userInput == "scissors" and userInput == "paper":
        print("you won!!!")
    elif userInput == "paper" and userInput == "rock":
        print("you won!!!")
        break
    else:
     print("you lost the game")

#!/usr/bin/env python3
#FreeCodeCamp Youtube Tutorial Chapter 10: Recursion
#Infinite ROCK, PAPER, SCISSORS!

# value = input('Please enter a value:\n')
# print(value)
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def play_rps():
    playerchoice = input(
        "\nROCK, PAPER, SCISSORS SHOOT!...\n1. Rock 🪨 \n2. Paper 📄 \n3. Scissors ✂️:\n\n")
    
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + playerchoice + ".")
    print("Python chose " + computerchoice + ".\n")

    if player == 1 and computer == 3:
        print("You win! 😁")
    elif player == 2 and computer == 1:
        print("You win! 😁")
    elif player == 3 and computer == 2:
        print("You win! 😁")
    elif player == computer:
        print("Tie game! 🤯")
    else:
        print("🐍 Python wins! 🐍")

    while True:
        playagain = input("\nPlay again?\nY for yes or Q to Quit\n").lower()
        if playagain not in ["y", "q"]:
            continue
        elif playagain == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            print("I hope you had as much fun as I did. Thanks for playing!\n")
            sys.exit("Bye!")


# Call the play_rps function to start the game
play_rps()

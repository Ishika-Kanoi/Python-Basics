# -*- coding: utf-8 -*-
"""
Game: Guess the number!
user inputs a number and computer inputs a number
user wins if its the same guess
"""

import random
print("Hello! Welcome to guess the number!")
print("You get 6 tries to guess a number")
num2=random.randint(1, 11)

for guesstaken in range(1,7):
    num1=int(input("Enter a Number between 1 to 10: "))
    
    if num1 == num2:
        print("Congratulations Player, You win!")
    elif num1<num2:
        print("Guess too low")
        print("Bwahaha!Computer wins, You can try again")
    elif num1>num2:
        print("Guess too High")
        print("Bwahaha!Computer wins, You can try again")
    else:
        pass
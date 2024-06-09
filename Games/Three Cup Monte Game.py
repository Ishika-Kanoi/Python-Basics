# -*- coding: utf-8 -*-
"""
Three Cup Monte Game
Game to learn how multiple functions interact with each other
"""
#game list
#user to guess where is letter 0
a=['','0','']

from random import shuffle

#shuffled_list =shuffle(a)
#shuffle does inplace shuffle
# call a to check 
#shuffle(a)
#a

def shuffle_cup(a):
    shuffle(a)
    return a

shuffled_list= shuffle_cup(a)

def player_guess():
    guess=''
    
    #while to check guess in 0,1,2
    while guess not in ['0','1','2']:
        guess= input("Where is the ball hidden?(choose from 0,1,2) ")
    
    return int(guess)

player_index=player_guess()

def check_guess(shuffled_list,player_index):
    if a[player_index] =='0':
        print("correct guess! you are lucky!")
    else:
        print("Wrong Guess!")
        print(a)
        
check_guess(shuffled_list, player_index)
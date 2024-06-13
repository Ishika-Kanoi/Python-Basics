# -*- coding: utf-8 -*-
"""
Write a program to create a dictionary containing names of Competition Winner students as 
keys and number of their wins as values
"""
Compw={}

n=eval(input("Enter the number of students that won in the competition?"))

for i in range(n):
    name=input("Enter the namee of the Winner: ")
    wins=eval(input("Enter the Number of Wins: "))
    Compw[name]=wins
    
print("This is your dictionary of winners and their wins: ",Compw)
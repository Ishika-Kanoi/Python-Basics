# -*- coding: utf-8 -*-
"""
Functions Introduction and Return keyword
"""

def hello():#def keyword allows you to createe a function
    print("hello ishika")
    print("Welcome to the game!")
hello()#function name calling

#Functions accept arguments
#value  stored in parameter is forgotten
def hello1(name):
    print('hello ' + name)
    
hello1('Spiderman!')
#print(name)#name not defined error as parameter is forgotten

def addfunc(num1,num2):
    print(num1,num2)
    return (num1+num2)

result= addfunc(3345,6583)
#9928

def addfunc1(num1,num2):
    print(num1+num2)
    
result1=addfunc1(2637263,8738)

#Result1and result are differe nt
#Result1 cannot save because it prints
#result returns a value to be saved
#Using return youy can save a value
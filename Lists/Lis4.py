# -*- coding: utf-8 -*-
"""
Write a program to read a list of n integers and find their median
If there are two middle values, return their average1
"""
lista = eval(input("Enter a list of integers"))
lista.sort()
print("Here is your sorted list", lista)
x=len(lista)

if x%2==0:
    half=x//2
    avg= (lista[half]+ lista[half-1])/2
    print("The median is ", avg)
else:
    avg= lista[(x//2)]
    print(" The median is ", avg)
    

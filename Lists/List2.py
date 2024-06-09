# -*- coding: utf-8 -*-
"""
Find minimum element from a list of elements
Also return its index

"""
lis1=eval(input("Enter a list"))
minimum= min(lis1)

for i in range(len(lis1)):
    if lis1[i]==minimum:
        index=i
        
print(f"This is your list: {lis1}\nThis is the minimum value {minimum} \nIts index is {index}")


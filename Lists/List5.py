# -*- coding: utf-8 -*-
"""
WAP to input a list of numbers and ask for a new element and its position.
Then insert the element at ivem position
"""
z= eval(input("Enter a list of numbers:"))
print(z)
new, pos =eval(input("Enter a new number and its position "))

z.insert(pos,new)

print(z)

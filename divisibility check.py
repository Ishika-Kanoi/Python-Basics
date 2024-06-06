# -*- coding: utf-8 -*-
"""
WAP to check divisibility"""
x= int(input(" enter first number "))
y=int(input(" enter second number "))

print(" We're going to check if one number is divisible with another! ")

if x%y == 0:
    print(f"{x} is divisible by {y}")
elif y%x==0:
    print(f'{y} is divisible by {x}')
else:
    print("they dont divide each other.")
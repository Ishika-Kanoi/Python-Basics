# -*- coding: utf-8 -*-
"""
Check if a program is leap year or not?

"""
year= int(input("enter year you want to check!"))

if year %100==0:
    if year%400==0:
        print("leap year")#century check
    else:
        print("century year")
elif year%4==0:
    print("leap Year")
else:
    print("Not a leap year")
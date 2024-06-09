# -*- coding: utf-8 -*-
"""
WAP  to input a list of numbers and swap elements 
at the even location with elements at odd location.
"""

val=eval(input("Enter a list: "))
print('list', val)
length=len(val)
length-=1
for i in range(0,length,2):
    val[i],val[i+1]=val[i+1],val[i]
    
print("Swapped list", val)
    
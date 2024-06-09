# -*- coding: utf-8 -*-
"""
Write a Program to geta list, replicate it twice and print the sorted list
in ascending and descending orders

"""
val=eval(input("Enter a list: "))
print("This is the list",val)
val=val*2
print("Here's your replicated list",val)
val.sort()
print("This is ascending order",val)
val.sort(reverse=True)
print("This is your descending order",val)

# -*- coding: utf-8 -*-
"""
Input 3 angles to determin if they form a triangle or not?

"""
angle1=int(input("Enter angle1 :"))
angle2= int(input("Enter angle2 :"))
angle3= int(input("Enter angle3 :"))

if (angle1+angle2+angle3) == 180:
    print("Yes they form a Triangle")
else:
    print("No they cannot form a Triangle")
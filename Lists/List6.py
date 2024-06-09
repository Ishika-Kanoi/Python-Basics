# -*- coding: utf-8 -*-
"""
WAP to input a list of numbers and ask for a new element and its position.
Then insert the element at ivem position
"""
z= eval(input("Enter a list of numbers:"))
print(z)
q=[]
M,N=eval(input("enter the values M and N "))

for i in range(len(z)):
    if z[i]%M==0:
        if z[i]%N==0:
            q.append(z[i])
    else:
        print(" Not divisible by M and N")
print(q)
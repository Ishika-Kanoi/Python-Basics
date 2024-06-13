# -*- coding: utf-8 -*-
"""
WAP to create a phone dictionary and print values in separate lines

"""
name=[]
no=[]

for x in range(5):
    Na,No=eval(input(" Enter name and Number: "))
    name.append(Na)
    no.append(No)

telephoned= {name[0]:no[0],name[1]:no[1],name[2]:no[2],name[3]:no[3],name[4]:no[4]}
for n in telephoned:
    print(n,":", telephoned[n])
    
#Check for values
if 22 in telephoned.values():
    print("The number exists in dictionary")
else:
    print("No 22 is not here! ")
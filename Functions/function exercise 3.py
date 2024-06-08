# -*- coding: utf-8 -*-
"""
1)WAF to find lesser of two numbers if both nubers are 
even, but returns greater if any one is odd

2)WAF that changes string to Master Yoda language.
I am free --> free am i

3) given a string return every charcter*3
hello--> hhheeellllllooo

4)Given a list of numbers return true ifthe array contains 3 next to a 3

5)Given a list of numbers, add only those which dont 
come between 6 and 9.

"""

def evenno(a,b):
    if (a%2==0)and (b%2==0):
        if a<b:
            return a
        else:
            return b
    else:
        if a>b:
            return a
        else:
            return b
        
#2

def master_yoda(lang):

    x=str.split(lang)
    op=x[::-1]
    return (" ".join(op))

#new

def thrice(str1):
    y=''
    for x in str1:
        y=y+(x*3)
        
    y=''.join(y)
    return y

def check3(alist):
    p=len(alist)-1
    for i in range(0,p):
        if alist[i:i+2]==[3,3]:
            return True

    return False
    
def summer_69(nums):

    sum1=0
    add=True
    for num in nums:
        while add:
            if num!=6:
                sum1=sum1+num
                break
            else:
                add=False
        while not add:
            if num!=9:
                break
            else:
                add=True
                break
    return sum1
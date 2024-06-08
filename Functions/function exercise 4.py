# -*- coding: utf-8 -*-
"""
1.WAF to compute volume of a spheregiven its radius
2. WAF to check if number is between range , inclusive of high and low
3. WAF that accepts a string and calculates the number of 
uppercase and lowecase letters.
4. WAF that takes a list and returns new list with unique elements from that
5. WAF to multiply all numbers in a list.
"""
#1
import math
def volsphere(rad):
    vol=(4/3)*math.pi*(rad*rad*rad)
    return vol
volsphere(2)

#2
def inclusive(a,b,c):
    if a>b and a<c:
        print(f'{a} is between {b} and {c}')

inclusive(5,2,7)

#3
def countcase(str1):
    lower=0
    upper=0
    for letter in str1:
        if letter>='a' and letter<='z':
            lower+=1
        else:
            upper+=1
    print(f'The number of lowercase letter are {lower}')
    print(f'The number of upper letter are {upper}')
    
countcase('This Is NOT a JOkE!')

#4

def unique(numbers):
    y=set(numbers)
    return y

unique([1,222,34,4,4,4,6,6,7,8,1,1])

#5
def mul(numb):
    i=1
    for x in numb:
        i=i*x
    return i
mul([1,2,3,-4])

# -*- coding: utf-8 -*-
"""
MAP,FILTER LAMBDA
"""
#map(func, iter1)
def square(num):
    return num**2

my_nuums = [1,2,3,4,5]

map(square,my_nuums)

for item in map(square,my_nuums):
    print(item)
    
list(map(square,my_nuums))

#with map you can either iterate or get  op in list

#FILTER only returns true values

def check_even(a):
    return a%2==0

list(filter(check_even, my_nuums))
#only returns true values

#LAMBDA

newsquare= lambda b: b**2
#newsquare(6)=36
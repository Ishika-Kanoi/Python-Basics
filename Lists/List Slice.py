# -*- coding: utf-8 -*-
"""
Extract two lists out of a given lis such that
1st list contains every other element from 5 to 15
2nd list contains every 4th element from the lis

display sum of elements in 1st slice
average of elements in 2nd slice

"""
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

slc1=list1[5:15:2]
slc2=list1[::4]

sum1=0
for every in slc1:
    sum1+=every

print(f"The 1st list is {slc1} , Their sum is {sum1}")

avg1= sum(slc2)/len(slc2)

print(f"The 2nd list is {slc2}, Their average is {avg1}")

# -*- coding: utf-8 -*-
"""Nested Dictionaries 
WAP that contains other dictionaries of what items 
guests are bringing to a picnic. The totalBrought()
function can read this data structure and calculate the
total number of an item being brought by all the guests.
"""
all_picnic= {' Arav': {'apples':5, 'knife':2},
             'Bishal': {'lemon':5,'chowmein':2,'disposal':6},
             'Kiran':{'sandwiches':6,'orange juice':7},
             'Riya': {'salad':3,'potato fries':7}
            }
def totalBrought(guests,item):
    totall=0
    for data,items in all_picnic.items():
        totall+= items.get(item,0)
    return totall

print("Number of things being bought are: ")
print("Apples  "+str(totalBrought(all_picnic,'apples')))
print("knife  "+str(totalBrought(all_picnic,'knife')))
print("lemon  "+str(totalBrought(all_picnic,'lemon')))
print("chowmein  "+str(totalBrought(all_picnic,'chowmein')))
print("sandwiches  "+str(totalBrought(all_picnic,'sandwiches')))
print("orange juice  "+str(totalBrought(all_picnic,'orange juice')))
print("salad  "+str(totalBrought(all_picnic,'salad')))
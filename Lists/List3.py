# -*- coding: utf-8 -*-
"""
WAP to find the numberof times an element occurs 
in the list
"""
list2=eval(input(("Enter a list")))
search= int(input("Enter the number you want to look for ?"))
count=0
for elements in range(len(list2)):
    
    if list2[elements]==search:
        count+=1
    else:
        pass
print(f"Element {search} occurs {count} times in the list")
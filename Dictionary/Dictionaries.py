# -*- coding: utf-8 -*-
"""
Dictionaries
{key: value pairs}

Dictionary keys should be immutable string, tuple or a number

WAP to read roll numbers and marks of four students
and creaate a dictionary from it having roll no as keys
"""
#Dictionary of teachers and their suvbject

Class8 ={'Maths': 'Dinesh Sir', ' English':'Rumpa Mam','Science':'Seema Mam','Hindi':'Brinda Mam','Social':'Prasenjit Sir'}

#Class8['Maths'] == 'Dinesh Sir'

roll=[]
marks=[]

for i  in range(4):
    rol,mark=eval(input("Enter Roll no and Marks. (Eg 1,100)"))
    roll.append(rol)
    marks.append(mark)
    
d={roll[0]:marks[0],roll[1]:marks[1],roll[2]:marks[2],roll[3]:marks[3]}

print("Created Dictionary: ",d)
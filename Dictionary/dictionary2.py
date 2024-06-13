# -*- coding: utf-8 -*-
"""
Write a program to create a dictionary name Numerals
from two lists

keys=['One','Two','three']
values=[11,2,3]
"""
keys=['One','Two','three']
values=[11,2,3]

Numerals=dict(zip(keys,values))
print("Numerals:" , Numerals)

#add elements to the list
#Keys should always be unique
Numerals['Four']=4

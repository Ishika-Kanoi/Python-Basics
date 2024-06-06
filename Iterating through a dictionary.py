# -*- coding: utf-8 -*-
"""
For Loops iteration in dictionary
"""
d = {'a1':11 , 'a2':22 , 'a3':33}

for key in d:
    print(key)

for item in d.items():
    print(item)

for item,value in d.items():
    print(value)
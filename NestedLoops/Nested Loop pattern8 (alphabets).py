# -*- coding: utf-8 -*-
"""
Nested loops:
    print pattern  8
A
AB
ABC
ABCD
ABCDE
    
"""
N= 65
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j), end=' ')
    print()
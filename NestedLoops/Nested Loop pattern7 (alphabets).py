# -*- coding: utf-8 -*-
"""
Nested loops:
    print pattern  7
A
B C
D E F
G H I J
K L M N O
    
"""
N= 65
for i in range(1,6):
    for j in range(1,i++1):
        print(chr(N), end=' ')
        N+=1
    print()
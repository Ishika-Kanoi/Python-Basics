# -*- coding: utf-8 -*-
"""
Check whether the given character is an Uppercase/Lowercase/digit/special
"""
a= input("enter the character")

if a>= 'A' and a<='Z':
    print("Uppercase character")
elif a>='a' and a<='z':
    print("Lowercase")
elif a>='0' and a<='9':
    print("Digit")
else:
    print("Special Character")
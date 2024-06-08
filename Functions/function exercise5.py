# -*- coding: utf-8 -*-
"""
1. WAF that checks palindrome
2. WAF to check a pangram
"""

def palindrome(s):
    s=s.replace(' ','')
    return s==s[::-1]

palindrome('helleh')            
palindrome('okokokos')
palindrome('nurses run')

import string
alphabet=string.ascii_lowercase
#gets all the alphabets
#2
def ispangram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    
    str1=str1.replace(' ','')
    str1=str1.lower()
    str1=set(str1)
    return str1==alphaset

ispangram("The quick brown fox is lazy over the dogand jumps")

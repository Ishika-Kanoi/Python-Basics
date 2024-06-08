# -*- coding: utf-8 -*-
"""
1) WAF that takes a two word string and returns true if both words begins
with same letter.

2)WAF that capitalises the 1st and 4th letter of a name
"""
def String_checker(a):
    x=a.split()
    print(a)
    if x[0][0]==x[1][0]:
        return True
    else:
        pass
    return False
String_checker('crunchy croissants')

def capitalise(name):
    
        y=list(name)
        y[0]=y[0].upper()
        y[3]=y[3].upper()
        
        y=''.join(y)
        return y
    
capitalise('hsgdsuhgbdijk')
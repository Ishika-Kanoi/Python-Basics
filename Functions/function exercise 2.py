# -*- coding: utf-8 -*-
"""
Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

Remember, don't run the function, simply provide the definition.

To give an idea what the function would look like when tested:

myfunc('Anthropomorphism')
# Output: 'aNtHrOpOmOrPhIsM'
"""
def myfunc(args):
    y=[]
    x=list(args)
    for each in range(len(x)):
        if each%2==0:
            y.append(x[each].upper())
        else:
            y.append(x[each])
    y=''.join(y)
    return y


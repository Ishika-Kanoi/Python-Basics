# -*- coding: utf-8 -*-
"""
__name__="__main__"

first file = one.py which contains func()

and a main statement that which tells if the program is running directly or imported]

another programs two.py imports one and we will know there that how 
the program is imported

one.py
"""
def func():
    print(" Func in one.py")
    
print("Top Level in One.py")

if __name__ == "__main__":
    print("One.py is run directly")
else:
    print("One.py is imported")
    
## output

#Top Level in One.py
##One.py is run directly
# -*- coding: utf-8 -*-
"""
program to demonstrate how 
__name__ == __main__ works

first file = one.py which contains func()

and a main statement that which tells if the program is running directly or imported]

"""

import one

print("Top level in two.py")

one.func()

if __name__ == "__main__":
    print("Two.py is run directly")
else:
    print("Two.py is imported!")
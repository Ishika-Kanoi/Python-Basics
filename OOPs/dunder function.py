# -*- coding: utf-8 -*-
"""
SPECIAL METHODS

"""
a=[1,2,3]
len(a)
str(a)
print(a)


class Book():
    def __init__(self,name,author,pages):
        self.name=name
        self.author=author
        self.pages=pages
    #adding dunder functions
    def __str__(self):
        return self.name+ " By " + self.author
    def __len__(self):
        return self.pages
    #delete with remark
    def __del__(self):
        print( "A book object is now deleted")
    
b = Book("The Alchemist", "Paul Coelho", 300)

b.author

str(b)
print(str(b))
len(b) #ERROR
#<__main__.Book object at 0x000001974DB55880>
#doesn't print what we want'
#so we change the str 

#after dunder function
str(b)
# Out[28]: 'The Alchemis By Paul Coelho'
len(b) #300


#suppose  
del b

print(b) #b not defined

#after changing the del func it throws a message now
#
#del b
#A book object is now deleted


# -*- coding: utf-8 -*-
"""
Create a class circle that contains the methods
we can use on it
"""

class Circle():
    
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*self.pi
        
    def perimeter(self):
        print("Perimeter :")
        return self.pi*2*self.radius
    
circle1=Circle()
#does not show error as defaut is set
circle2=Circle(22)

#calculated default for =1
circle1.area
circle1.perimeter()

circle2.area
circle2.perimeter()

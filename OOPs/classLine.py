# -*- coding: utf-8 -*-
"""
Declare a class Line which calculates sole and 
distance of the line
"""
import math

class Line:
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
        
    def slope(self):
        x1,y1= self.coor1
        x2,y2= self.coor2
        m=(y2-y1)/(x2-x1)
        return (f"Slope is  {m}")
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        d=math.sqrt(((x2-x1)**2)+(y2-y1)**2)
        return d
c1=(3,2)
c2=(8,10)         
Line1=Line(c1,c2)

Line1.coor1
Line1.slope()
Line1.distance()
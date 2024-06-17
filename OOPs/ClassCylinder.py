# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:36:29 2024

@author: hp
"""

class cylinder:
    pi = 3.14
    
    def  __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        
    def surface_area(self):
        return ((2*self.pi*self.radius*self.height) + (2*self.pi*self.radius*self.radius))
    
    def volume(self):
        return self.pi*self.radius*self.radius*self.height
    
Cylinder1=cylinder(2,3)

Cylinder1.height
Cylinder1.volume()
Cylinder1.surface_area()

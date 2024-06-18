# -*- coding: utf-8 -*-
"""
POLYMORPHISM
"""

class Dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "Woof, I am " + self.name

class Cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "Meow , I am " + self.name
#two classes with same methods
#creating objects 
Niko=Dog('Niko')
Felix= Cat('felix')

print(Niko.speak())

print(Felix.speak())

#Inspite of having the same method names
#These are unique to its own class
#Loop to show polymorphism
for  pet in [Niko,Felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())
    
pet_speak(Niko)
pet_speak(Felix)

#Base Class
class Animal():
    def __init__(self,name):
        self.name=name
    #Abstract Method
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")
#just to demonstrate the base class
#my_animal = Animal('fred')
#my_animal.speak()

#BASE CLASS should Inherit 

class Cat(Animal):
    def speak(self):
        return self.name + "  says Meeeow!"
    
Iris = Cat("Iris")
Iris.speak()

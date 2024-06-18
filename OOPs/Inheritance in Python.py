# -*- coding: utf-8 -*-
"""
Inheritance and Polymorphism.

Inheriting from one class is helpful as you dont
need to write code again for functions you need again

if you inherit from class A , you can also ovveride the functions
Here we over=rid the eat method 

"""
#created a parent classs
class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("i Am an ANimal")
    def eat(self):
        print("I am eating")
#dog inherits animal     
class Dog(Animal):
    def __init__(self):
        #create instance of animal class as i inherited from animal
        Animal.__init__(self)
        print("Dog Created")
        
    def who_am_i(self):
        print("I am Dog")
    #adding more functions
    def bark(self):
        print("Woff!")
    def eat(self):
        print('i am a dog eating Chimken')
        
my_dog=Dog()
my_cat=Animal()
#prints animal created  and dog created
#we can use who am i and eat in my_dog

my_dog.eat()
my_dog.who_am_i()

#Overriding a method prints i am dog
my_dog.who_am_i()

#cat is another object of animal, OG
my_cat.who_am_i()

#new functions
my_dog.bark()

my_dog.eat()
my_cat.eat()

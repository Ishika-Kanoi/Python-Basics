# -*- coding: utf-8 -*-
"""
Create a Bank account object
with a couple of attributes, methods and special methods

attributes - owner, balance
methods - deposit, withdraw

withdrawals should not exceed a minimum balance

"""

class Account():
    def __init__(self,owner,balance=5000):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,x):
        print(f"You just made a depsoit of {x}. \n Your balance is ")
        self.balance+= x
        return self.balance
    def withdraw(self,y):
        print(f"You are now withdrawing {y} , Your balance is  {self.balance}" )
        if y>self.balance:
            print ("Amount exceeds minimum balance, Cannot witdraw")
        else:
            self.balance-=y
            return self.balance
        
    def __str__(self):
        return "Account Owner :" + str(self.owner) + "\nAccount balance : $"  + str(self.balance)
        
acc1= Account('Ish=ika',30000)
acc1.balance
acc1.deposit(500)
acc1.balance
acc1.withdraw(500)

print(acc1)
acc1.withdraw(40000)
acc1.balance

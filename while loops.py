# -*- coding: utf-8 -*-
"""
WHILE LOOPS BREAK CONTINUE
"""
#a=10
#while a>5:
#    if a==7:
#        break
#    print(a)
#    a=a-1
#print('done')#

while True:
      print('Who are you?')
      name = input()
      if name != 'Joe':
          continue
      print('Hello, Joe. What is the password? (It is a fish.)')
      password = input()
      if password == 'swordfish':
         break
print('Access granted.')   
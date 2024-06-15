# -*- coding: utf-8 -*-
"""
If you import the pprint module into your programs, you’ll have access to the pprint()
 and pformat() functions that will “pretty print” a dictionary’s values.
 This is helpful when you want a cleaner display of the items in a dictionary
 than what print() provides.
"""

import pprint

message = 'It was a bright day in june and the butterflies were enjoying sweetnectar from flowers'

count={}


for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
print(count)
#difference with pprint

pprint.pprint(count)

import json
print(json.dumps(count,indent=2))

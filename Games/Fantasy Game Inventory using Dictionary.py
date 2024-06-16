# -*- coding: utf-8 -*-
"""
Fantasy Game Inventory

Players inventory will be a dictionary, where 
keys are strings and values are items.
Value is an integer that descirbes how many items the player has
For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
"""

d={'rope':1,'torch':6, 'gold coin':500 , 'dagger':2,'arrow':15}
d.setdefault('item',0)

def display_inventory(d):
    print("Inventory: ")
    for things,count in d.items():
        print(f'{things}  :' + str(count))
print("   ORIGINAL    ")
display_inventory(d)

"""
Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:
"""
def addtoinventory(inventory, added_items):
    z=list(set(added_items))
    for c in z:
        d[c]=0
    return d        
        
#let d be our inventory
dragonLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

d=addtoinventory(d, dragonLoot)
print("    New Inventory    ")
display_inventory(d)

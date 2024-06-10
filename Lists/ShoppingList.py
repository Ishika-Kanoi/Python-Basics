# -*- coding: utf-8 -*-
"""
Create a Shopping list.
"""
def shopping_list():
    spam=[]

    print(f"Hi, This is your shopping list! {spam}")

    add=True

    while add:
   
        if add:
            item= input("Add your items here : ")
            print("hmm..")
            spam.append(item)
            choice=input('Do you want to add more,Y or N? ')
            if choice=='Y':
                continue
            else:
                add=False
                print("Here is your list!",spam)
                break
        else:
            pass
    return spam

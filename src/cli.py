"""
inventory app which:
    stores data in file
    uses command line for:
        add
        update
        list
        delete
            id
            name
            cond
            ?checked_out?
"""
from models.item import Item
items=[]#used to store items(input from add_item)
next_id=0

def menu1(): #first user menu
    print("""
    1. List all Items
    2. Add Item
    3. Update Item
    4. Delete Item
    5. Exit
    """)

def list_items(): #lists all items in items[]
    print('list_items')
    for item in items:
        print(item)
        print('')

def add_item(): #creates item using the item class, then adds it to items[]
    global next_id
    print('add_item')
    name=input('Name: ')
    cond=input('Condition: ')
    item_id=next_id
    next_id+=1
    
    tmp=Item(name, cond, item_id)
    items.append(tmp)


def update_existing():
    print('update_existing')
    if not items:  #when empty, items is False, so for the if to fire, we must make it true
        print('No items exist')
        return
    list_items()
    try:
        item_id_update=int(input(f'ID of item to update:\n> '))
    except Exception:
        print('invalid input')
        return
    
    for item in items:
        if item.item_id==item_id_update:
            item.name=input('Name: ')
            item.cond=input('Condition: ')
            break

    else:
        print('Item not found')
        
    


def delete_item():
    print('delete_item')
    if not items:
        print('No items exist')
        return
    list_items()
    try:
        item_id_delete=int(input(f'ID of item to delete:\n> '))
    except Exception:
        print('invalid input')
        return
    for index,item in enumerate(items):
        if item.item_id==item_id_delete:
            index_remove=index
            break

    else:
        print('Item not found')
        return
    
    print(f"item:\n{items.pop(index_remove)}\nHas been removed")


print("""
******************************************
*      \/EAH                             *
*      /   BABY                          *
*                                        *
******************************************


""")
"""note on try/except input validation/error catching
while(True): #always
    menu1()
    try:
        in1=int(input(">"))
    except Exception:
        input('Invalid Input, press enter to try again')
        continue
    if in1==1:
        pass
    elif in1==2:
        pass
    elif in1==3:
        pass
    elif in1==4:
        pass
    elif in1==5:
        exit()
    else:
        print('Improper Input, please try again')
        continue
"""

while(True): #always
    menu1()
    in1=input(">")
    if in1=="1":
        list_items()
    elif in1=="2":
        add_item()
    elif in1=="3":
        update_existing()
    elif in1=="4":
        delete_item()
    elif in1=="5":
        exit()
    else:
        print('Improper Input, please try again')
        continue


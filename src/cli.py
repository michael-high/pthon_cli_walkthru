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
# TODO make a menu print out showing options
#variables
items=[1,2,3]

def menu1():
    print("""
    1. List all Items
    2. Add Item
    3. Update Item
    4. Delete Item
    5. Exit
    """)

def list_items():
    print('list_items')
    for item in items:
        print(item)

def add_item():
    print('add_item')
    global next_id
    name=input('Name: ')
    cond=input('Condition: ')
    item_id=next_id
    next_id+=1


def update_existing():
    print('update_existing')

def delete_item(itemId):
    print('delete_item')

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


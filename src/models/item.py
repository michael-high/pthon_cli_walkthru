#items have name, cond, id
class Item:
    def __init__(self, name, condition,item_id,):
        self.name=name
        self.condition=condition
        self.item_id=item_id
    def __str__(self):
        return f'Name: {self.name}\nCondition: {self.condition}\nItem ID: {self.item_id}'

if __name__=="__main__":
    item_one=Item("book", 'used',0)
    item_two=Item("bottle", 'new',1)
    print(item_one)
    print(item_two.item_id)
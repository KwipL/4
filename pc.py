class Item:
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other,Item):
            return self.price + other.price
        elif isinstance(other,int):
            return self.price + other

    def __radd__(self, other):
        if isinstance(other,Item):
            return self.price + other.price
        elif isinstance(other,int):
            return self.price + other

item1 = Item('Процессор',15_000,0.2)
item2 = Item('Видеокарта',30_000,0.9)
item3 = Item('ОЗУ',8000,0.5)

total_sum = item1 + item2 + item3
print(total_sum)
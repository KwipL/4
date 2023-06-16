class Item:
    def init(self, price, weight):

        self.price = price
        self.weight = weight

def __sub__(self, other):
    new_price = self.price - other.price
    new_weight = self.weight - other.weight
    return Item(new_price, new_weight)


def __mul__(self, other):
    new_price = self.price * other
    new_weight = self.weight * other
    return Item(new_price, new_weight)


def __truediv__(self, other):
    new_price = self.price / other
    new_weight = self.weight / other
    return Item(new_price, new_weight)

item1 = Item(100, 1)
item2 = Item(50, 0.5)

item3 = item1 - item2
print(item3.price, item3.weight)

item4 = item1 * 2
print(item4.price, item4.weight)

item5 = item1 / 2
print(item5.price, item5.weight)
class Bicycle(object):
    def __init__(self, name, weight, cost_produce):

        self.name = name
        self.weight= weight
        self.cost_produce = cost_produce

class Bike_Shop(object):
    def __init__(self, name, inventory, markup):
        self.name = name
        self.inentory = inventory
        self.markup = .20


class Customer(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money


shop_inventory =[
Bicycle("Speedster",20,200),
Bicycle("Cruiser",25,100),
Bicycle("Flyer",22,150),
]

customers = [
Customer("John",800),
Customer("Mary",1000),
Customer("Rob", 500),
]


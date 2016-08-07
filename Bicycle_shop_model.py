class Bicycle(object):
    def __init__(self, name, weight, cost_produce):

        self.name = name
        self.weight= weight
        self.cost_produce = cost_produce

class Bike_Shop(object):
    def __init__(self, name, inventory, markup, profit):
        self.name = name
        self.inventory = inventory
        self.markup = .20
        self.profit = 0

    def profit(cost):
        markup = .20
        print(cost * markup)

class Customer(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money
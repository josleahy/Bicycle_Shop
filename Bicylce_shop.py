class Bicycle(object):
    def __init__(self, model, weight, cost_produce):
        self.model = ''
        self.weight = 0
        self.cost_produce = 0

class Bike_Shops(object):
    def __init__(self, name, inventory, markup):
        self.name = "Joe's Bike Shop"
        self.inentory = 0
        self.markup = Bicycle.cost_produce + (Bicycle.cost_produce * .20)

class Customer(object):
    def __init__(self, name, money,):
        self.name = ""
        self.money = 0


    def buy_bike(self):
        #Customer money becomes money - cost of the bike
        #Bike_Shop inventory - 1

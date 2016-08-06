class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = ''
        self.weight = 0
        self.cost = 0

class Bike_Shops(object):
    def __init__(self, name, inventory):
        self.name = "Joe's Bike Shop"
        self.inentory = 0

    def profit_margin(self):
        margin = Bicycle.cost * .20
    # 20% profit on bike sales

class Customer(object):
    def __init__(self, name, budget):
        self.name = ""
        self.budget = 0

    def buy_bike(self):
        #Customer budget becomes budget - cost of the bike
        #Bike_Shop inventory - 1

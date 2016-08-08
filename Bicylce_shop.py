from Bicycle_shop_model import Bicycle, Bike_Shop, Customer

shop_inventory =[
Bicycle("Speedster",20,200),
Bicycle("Cruiser",25,100),
Bicycle("Flyer",22,150),
Bicycle("XL", 28, 175),
Bicycle("Sport", 23, 180)
]

shop = Bike_Shop("Joe's Bike Shop", shop_inventory, .20, 0)

customers = [
Customer("John",800),
Customer("Mary",1000),
Customer("Rob", 500),
]

print ("Our Current Inventory")
print ("-" * 20)
for bike in range(len(shop_inventory)):
     print (shop_inventory[bike].name)
print ("-" * 20)

print("Customers")
print("-" * 20)
for customer in range(len(customers)):
    print(customers[customer].name)

print("-" * 20)
print("Who can afford what?")
print("-" * 20)
for customer in range(len(customers)):
    for bike in range(len(shop_inventory)):
        if shop_inventory[bike].cost_produce <= customers[customer].money:
            print ("{0} can afford the: {1}".format(customers[customer].name, shop_inventory[bike].name))

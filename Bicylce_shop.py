from Bicycle_shop_model import Bicycle, Bike_Shop, Customer
shop_inventory =[
Bicycle("Speedster",20,1000),
Bicycle("Cruiser",25,200),
Bicycle("Flyer",22,600),
Bicycle("XL", 28, 100),
Bicycle("Sport", 23, 500)
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
     print (shop_inventory[bike].name + "(" + str(shop_inventory[bike].weight) + " lbs.) - " + "$" + str(shop_inventory[bike].cost_produce))
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

print("-" * 20)
print("How much will Joe's profit for each bike sold?")
print("-" * 20)


for bike in range(len(shop_inventory)):
    profit = shop_inventory[bike].cost_produce * .20
    print(shop_inventory[bike].name + ' - $' + str(profit))



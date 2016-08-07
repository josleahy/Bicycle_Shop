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

print("Welcome to " + shop.name + "!")
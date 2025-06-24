from cart import *

phone1 = Phone("Phone x", 1000, "red")
tv1 = Tv("Tv y", 2034, 64)

cart1 = Cart()
cart1.add_product(phone1)
cart1.add_product(tv1)
cart1.add_product(tv1)
cart1.add_product("test")
print(cart1)
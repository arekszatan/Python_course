from products import *

class Cart:
    def __init__(self):
        self.__products_list = []
        self.__cart_value = 0

    def add_product(self, product):
        #if isinstance(product, Phone) or isinstance(product, Tv):
        if isinstance(product, Product):
            if product not in self.__products_list:
                self.__products_list.append(product)
                self.__calculate_cart()

    def __calculate_cart(self):
        self.__cart_value = 0
        for el in self.__products_list:
            self.__cart_value += el.price

    def __str__(self):
        str_data = "\nCart info, products list:"
        for product in self.__products_list:
            str_data += "\n - " + str(product.name) + " " + str(product.price)
        str_data += "\n cart value: " + str(self.__cart_value)
        return str_data

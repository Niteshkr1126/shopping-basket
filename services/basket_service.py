from typing import Dict
from exception import exceptions


class BasketService:
    basket_items = Dict[str, int]

    def __init__(self):
        self.basket_items = {}

    def get_basket(self):
        return self.basket_items

    def add_product(self, product_code: str):
        if product_code in self.basket_items:
            self.basket_items[product_code] = self.basket_items[product_code] + 1
        else:
            self.basket_items[product_code] = 1
        return self.basket_items

    def add_product_with_quantity(self, product_code: str, quantity: int):
        if product_code in self.basket_items:
            self.basket_items[product_code] = self.basket_items[product_code] + quantity
        else:
            self.basket_items[product_code] = quantity
        return self.basket_items

    def remove_product(self, product_code: str):
        try:
            del self.basket_items[product_code]
        except Exception:
            print(exceptions.ProductDoesNotExist().message)
        return self.basket_items

    def view_basket(self):
        for product_code in self.basket_items:
            print(f'Product Code: {product_code}\tQuantity: {self.basket_items[product_code]}')

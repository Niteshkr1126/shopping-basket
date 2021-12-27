from typing import Dict
from exception import exceptions
from models.product import Product


def apply_delivery_charges(amount):
    if amount < 50:
        ProductService.delivery_charge = 4.95
    if 50 <= amount < 90:
        ProductService.delivery_charge = 2.95
    if amount >= 90:
        ProductService.delivery_charge = 0


def apply_offers(basket_items, products):
    discount_amount = 0
    if "R01" in basket_items and basket_items.get("R01") > 1:
        discount_qty = basket_items.get("R01")//2
        discount_amount = discount_qty * (products.get("R01").price/2)
    ProductService.discount_amount = discount_amount


class ProductService:
    products = Dict[str, Product]
    delivery_charge = 0
    discount_amount = 0

    def __init__(self):
        self.products = {}

    def get_product(self, product_code):
        if product_code not in self.products:
            raise exceptions.ProductDoesNotExist()
        return self.products.get(product_code)

    def add_product(self, product: Product):
        if product.code in self.products:
            raise exceptions.ProductAlreadyExist()
        self.products[product.code] = product
        return product

    def remove_product(self, product_code: str):
        try:
            del self.products[product_code]
        except Exception:
            print(exceptions.ProductDoesNotExist().message)

    def show_products(self):
        for product in self.products.values():
            print(f'{product.code}\t{product.name}\t{product.price}')

    def get_total(self, basket_items):
        total = 0
        for product_code in basket_items:
            product = self.get_product(product_code)
            total += product.price * basket_items.get(product_code)
        apply_offers(basket_items, self.products)
        total -= ProductService.discount_amount
        apply_delivery_charges(total)
        total += ProductService.delivery_charge
        total -= total % 0.01
        return "${:.2f}".format(total)

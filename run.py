from models.product import Product
from services import basket_service, product_service


def run():
    # Create the product objects
    red_widget = Product(code="R01", name="Red Widget", price=32.95)
    green_widget = Product(code="G01", name="Green Widget", price=24.95)
    blue_widget = Product(code="B01", name="Blue Widget", price=7.95)

    # Add the above products to the product catalogue
    product_catalogue_service = product_service.ProductService()
    product_catalogue_service.add_product(red_widget)
    product_catalogue_service.add_product(green_widget)
    product_catalogue_service.add_product(blue_widget)

    # Display all the available products from product catalogue
    print("Available Products:")
    product_catalogue_service.show_products()
    print("\n")

    # Initialize the basket as per example 1
    my_basket_service1 = basket_service.BasketService()
    # Add products to the basket
    my_basket_service1.add_product("B01")
    my_basket_service1.add_product("G01")
    # View Basket Items
    print("Basket 1 Items:")
    my_basket_service1.view_basket()
    my_basket1 = my_basket_service1.get_basket()
    # Get total for basket after applying offers and then delivery charges
    total1 = product_catalogue_service.get_total(my_basket1)
    print("Basket total: " + total1)
    print("\n")

    # Initialize the basket as per example 2
    my_basket_service2 = basket_service.BasketService()
    # Add products to the basket
    my_basket_service2.add_product("R01")
    my_basket_service2.add_product("R01")
    # View Basket Items
    print("Basket 2 Items:")
    my_basket_service2.view_basket()
    my_basket2 = my_basket_service2.get_basket()
    # Get total for basket after applying offers and then delivery charges
    total2 = product_catalogue_service.get_total(my_basket2)
    print("Basket total: " + total2)
    print("\n")

    # Initialize the basket as per example 3
    my_basket_service3 = basket_service.BasketService()
    # Add products to the basket
    my_basket_service3.add_product("R01")
    my_basket_service3.add_product("G01")
    # View Basket Items
    print("Basket 3 Items:")
    my_basket_service3.view_basket()
    my_basket3 = my_basket_service3.get_basket()
    # Get total for basket after applying offers and then delivery charges
    total3 = product_catalogue_service.get_total(my_basket3)
    print("Basket total: " + total3)
    print("\n")

    # Initialize the basket as per example 4
    my_basket_service4 = basket_service.BasketService()
    # Add products to the basket
    my_basket_service4.add_product_with_quantity("B01", 2)
    my_basket_service4.add_product_with_quantity("R01", 3)
    # View Basket Items
    print("Basket 4 Items:")
    my_basket_service4.view_basket()
    my_basket4 = my_basket_service4.get_basket()
    # Get total for basket after applying offers and then delivery charges
    total4 = product_catalogue_service.get_total(my_basket4)
    print("Basket total: " + total4)
    print("\n")


if __name__ == '__main__':
    run()

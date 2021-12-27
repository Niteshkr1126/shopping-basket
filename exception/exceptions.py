class ProductAlreadyExist(Exception):
    message = 'Product already exists'


class ProductDoesNotExist(Exception):
    message = 'Product doesn\'t exists'

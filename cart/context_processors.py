"""
Contxt Processor for the shopping cart
"""
from .cart import Cart


def cart(request):
    """
    Instantiate Cart and make it available as the
    variable named "cart"
    """
    return {"cart": Cart(request)}

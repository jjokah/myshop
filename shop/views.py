"""
Views for the shop app
"""

from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list(request, category_slug=None):
    """This view returns the list of all products or
        products within a category if specified.
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        "shop/product/list.html",
        {"category": category, "categories": categories, "products": products},
    )


def product_detail(request, id, slug):
    """Retrieve and display a single product
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        "shop/product/detail.html",
        {"product": product, "cart_product_form": cart_product_form},
    )

"""
Manage orders in the shop
"""

from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from coupons.models import Coupon
from shop.models import Product


class Order(models.Model):
    """ Stores infomation about the customer making order """

    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    email = models.EmailField(_("email"))
    address = models.CharField(_("address"), max_length=250)
    postal_code = models.CharField(_("postal_code"), max_length=20)
    city = models.CharField(_("city"), max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    coupon = models.ForeignKey(
        Coupon, related_name="orders", null=True, blank=True, on_delete=models.SET_NULL
    )
    discount = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost_before_discount(self):
        """ Returns the total cost of items before discount. """

        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost

    def get_discount(self):
        if self.coupon:
            return (
                self.discount / Decimal(100)
            ) * self.get_total_cost_before_discount()
        return Decimal(0)

    def get_total_cost(self):
        """ Returns the total cost of items. """

        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal(100))


class OrderItem(models.Model):
    """ Stores the product, quantity, and price paid for each item """

    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        """ Returns the total cost of each item """

        return self.price * self.quantity

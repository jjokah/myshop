"""
This module provide forms to be used in the cart application
"""
from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    """
    A form to add products to cart.
    """

    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_("Quantity")
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )

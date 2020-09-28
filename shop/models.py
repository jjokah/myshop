"""
This module holds models of every object in the shop.
"""


from django.db import models
from django.urls import reverse

from cloudinary.models import CloudinaryField


class Category(models.Model):
    """ The category model each product is classified into. """

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Retrieve url for list of product in a given category"""
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """ The product model of an item in the shop. """

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = CloudinaryField("product")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Retrieves url for a given product"""
        return reverse("shop:product_detail", args=[self.id, self.slug])

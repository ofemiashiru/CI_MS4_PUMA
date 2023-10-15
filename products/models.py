from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    class Meta:

        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    brand = models.ForeignKey(
        Brand, null=False, blank=False, on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)

    is_accessory = models.BooleanField(null=False, blank=False, default=False)

    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    new_arrival = models.BooleanField(null=False, blank=False, default=False)
    deal = models.BooleanField(null=False, blank=False, default=False)
    clearance = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name

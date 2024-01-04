from django.db import models


class Product(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    brandName = models.CharField(max_length=100)
    regularPrice = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name

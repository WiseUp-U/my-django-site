from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    available = models.BooleanField(default=True)
    year = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images")
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.product.name
    

from django.db import models

# Create your models here.
class Products(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default='All Products are Amazing')

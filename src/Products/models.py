from django.db import models

# Create your models here.
class Products(models.Model):
    productNumber = models.AutoField(primary_key=True)
    category    = models.CharField(max_length=100, blank=False)
    title       = models.CharField(max_length=80, blank=False)
    description = models.TextField(blank=False)
    price       = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    summary     = models.TextField(default='All Products are Amazing')
    available   = models.BooleanField(default=True)

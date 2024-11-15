from django.db import models

# Create your models here.
class Students(models.Model):
    registrationNumber = models.CharField(max_length=50, blank=False)
    firstName = models.CharField(max_length=50, blank=False)
    middleName = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=False)
    courseName = models.CharField(max_length=100)
    feedback = models.TextField(help_text="Enter your feedback here based on the course you're doing")


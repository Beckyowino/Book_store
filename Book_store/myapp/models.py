from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
import datetime

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='Book_store/images/')

    def __str__(self):
        return self.title

class Event(models.Model):
    summary = models.CharField(max_length=255, default="")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class PricingPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

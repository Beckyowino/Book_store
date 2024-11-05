from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils import timezone

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

class PricingPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200, default='Untitled Event')
    description = models.TextField(default='No description provided.')
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now().time())
    location = models.CharField(max_length=255, default='Location not specified.')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title

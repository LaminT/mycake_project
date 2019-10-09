from django.db import models
from datetime import datetime
from bakers.models import Baker


class Listing(models.Model):
    baker = models.ForeignKey(Baker, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    ingredients = models.CharField(max_length=100)
    flour = models.DecimalField(max_digits=2, decimal_places=1)
    sugar = models.DecimalField(max_digits=2, decimal_places=1)
    eggs = models.DecimalField(max_digits=2, decimal_places=1)
    butter = models.DecimalField(max_digits=2, decimal_places=1)
    oil = models.DecimalField(max_digits=2, decimal_places=1)
    margarine = models.DecimalField(max_digits=2, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

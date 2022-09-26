from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200)
    mail = models.EmailField(blank=True)
    registry_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    show = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='photos/%y/%m')

    def __str__(self):
        return self.name

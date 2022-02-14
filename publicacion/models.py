from turtle import title
from django.db import models

# Create your models here.


class Business(models.Model):
    business = models.CharField(max_length=100)

    def __str__(self):
        return self.business


class Publicacion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    direccion = models.CharField(max_length=255)
    price = models.IntegerField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

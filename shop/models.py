from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class Category_fb(models.Model):
    category = models.CharField(name="Категория fb accaunt", max_length=128, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    available = models.BooleanField(default=True, verbose_name="Существует")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product_fb(models.Model):
    name = models.CharField(name="name", max_length=128, db_index=True)
    modal = models.CharField(name="modal", max_length=128)
    category = models.ForeignKey(Category_fb, models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    file = models.FileField(db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    available = models.BooleanField(default=True, verbose_name="Доступен")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name


class Category_offer(models.Model):
    category = models.CharField(name="Категория", max_length=128, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    available = models.BooleanField(default=True, verbose_name="Существует")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)


    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product_offer(models.Model):
    name = models.CharField(name="name", max_length=128, db_index=True)
    modal = models.CharField(name="modal", max_length=128)
    category = models.ForeignKey(Category_fb, models.CASCADE)
    img = models.ImageField(name="image")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    file = models.FileField(db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    available = models.BooleanField(default=True, verbose_name="Доступен")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name




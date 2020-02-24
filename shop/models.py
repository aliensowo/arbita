from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class Category(models.Model):
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


class Product(models.Model):
    name = models.CharField(name="name", max_length=128, db_index=True)
    category = models.ForeignKey(Category, models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    #url = models.URLField(unique=True)
    file = models.FileField(db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name


# class bd_account_bm(models.Model):
#     name = models.CharField(name="Аккаунты БМ", db_index=True)
#     url = models.URLField(unique=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     stock = models.PositiveIntegerField(verbose_name="На складе")
#     available = models.BooleanField(default=True, verbose_name="Доступен")
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['name']
#         index_together = [
#             ['id', 'slug']
#         ]
#
#     def __str__(self):
#         return self.name
#
#     # def get_absolute_url(self):
#     #     return reverse('shop:UpCategoryList', args=[self.slug])
#
#
# class bd_account_rec(models.Model):
#     name = models.CharField(name="Рек аккаунты", db_index=True)
#     url = models.URLField(unique=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     stock = models.PositiveIntegerField(verbose_name="На складе")
#     available = models.BooleanField(default=True, verbose_name="Доступен")
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['name']
#         index_together = [
#             ['id', 'slug']
#         ]
#
#     def __str__(self):
#         return self.name
#
#
# class bd_photoshop_ooo(models.Model):
#     name = models.CharField(name="Фотошоп ООО", db_index=True)
#     url = models.URLField(unique=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     stock = models.PositiveIntegerField(verbose_name="На складе")
#     available = models.BooleanField(default=True, verbose_name="Доступен")
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['name']
#         index_together = [
#             ['id', 'slug']
#         ]
#
#     def __str__(self):
#         return self.name
#
#
#
# class bd_photoshop_ip(models.Model):
#     name = models.CharField(name="Фотошоп ИП", db_index=True)
#     url = models.URLField(unique=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     stock = models.PositiveIntegerField(verbose_name="На складе")
#     available = models.BooleanField(default=True, verbose_name="Доступен")
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['name']
#         index_together = [
#             ['id', 'slug']
#         ]
#
#     def __str__(self):
#         return self.name
#
#
# class bd_photoshop_office(models.Model):
#     name = models.CharField(name="Фотошоп Офис", db_index=True)
#     url = models.URLField(unique=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     stock = models.PositiveIntegerField(verbose_name="На складе")
#     available = models.BooleanField(default=True, verbose_name="Доступен")
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['name']
#         index_together = [
#             ['id', 'slug']
#         ]
#
#     def __str__(self):
#         return self.name
#
#
# class bd_other_proxy(models.Model):
#     name = models.CharField(name="Прокси", db_index=True)
#     url = models.URLField(unique=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     stock = models.PositiveIntegerField(verbose_name="На складе")
#     available = models.BooleanField(default=True, verbose_name="Доступен")
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['name']
#         index_together = [
#             ['id', 'slug']
#         ]
#
#     def __str__(self):
#         return self.name
#
#
# class bd_other_bankcard(models.Model):
#     name = models.CharField(name="Банковские карты", db_index=True)
#     url = models.URLField(unique=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     stock = models.PositiveIntegerField(verbose_name="На складе")
#     available = models.BooleanField(default=True, verbose_name="Доступен")
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['name']
#         index_together = [
#             ['id', 'slug']
#         ]
#
#     def __str__(self):
#         return self.name
#
#
# class bd_promo_company(models.Model):
#     name = models.CharField(name="Компании", db_index=True)
#     url = models.URLField(unique=True)
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)
#     stock = models.PositiveIntegerField(verbose_name="На складе")
#     available = models.BooleanField(default=True, verbose_name="Доступен")
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['name']
#         index_together = [
#             ['id', 'slug']
#         ]
#
#     def __str__(self):
#         return self.name
#

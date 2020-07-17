from django.contrib import admin
from .models import Product_fb, Category_fb
from .models import Product_offer, Category_offer

# Модель товара
class Product_fbAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'file']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}


class Category_fbAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class Product_offerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', 'file', 'image']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}


class Category_offerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category_fb, Category_fbAdmin)
admin.site.register(Product_fb, Product_fbAdmin)
admin.site.register(Category_offer, Category_offerAdmin)
admin.site.register(Product_offer, Product_offerAdmin)
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.utils.html import format_html
from django.db import models
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(ModelAdmin):

    def ProductPhoto(self, object):
       return format_html('<img src="{} "width="50">'.format(object.images.url))

    prepopulated_fields  = {'slug': ('product_name',)}
    list_display         = ('id', 'ProductPhoto', 'product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    list_display_links   = ('id', 'ProductPhoto')
    list_editable        = ('is_available',)
    ordering             = ('id',)
    


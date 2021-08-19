from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from django.db import models
from .models import Product, Variation
# Register your models here.
@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, ModelAdmin):

    def ProductPhoto(self, object):
       return format_html('<img src="{} "width="50">'.format(object.images.url))

    prepopulated_fields  = {'slug': ('product_name',)}
    list_display         = ('id', 'ProductPhoto', 'product_name', 'price', 'stock', 'category', 'modified_date', 'is_available', 'is_popular')
    list_display_links   = ('id', 'ProductPhoto')
    list_editable        = ('is_available', 'is_popular')
    ordering             = ('id',)


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
   list_display = ('id', 'product', 'variation_category', 'variation_value', 'created_date', 'is_active')
   ordering = ('id',)
   list_editable = ('is_active',)    


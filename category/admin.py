from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Category
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class CategoryAdmin(ImportExportModelAdmin, ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('id', 'category_name', 'slug', 'created_date')
    list_filter = ('id', 'category_name', 'created_date')
    list_display_links = ('id', 'category_name')
admin.site.register(Category, CategoryAdmin)

from django.db import models
from category.models import Category


class Product(models.Model):
    product_name   = models.CharField(max_length=200, unique=True)
    slug           = models.SlugField(max_length=200, unique=True)
    description    = models.TextField(max_length=500, blank=True)
    price          = models.IntegerField()
    images         = models.ImageField(upload_to = 'media/product/%y/')
    stock          = models.IntegerField()
    is_available   = models.BooleanField(default=True)
    category       = models.ForeignKey(Category, on_delete = models.CASCADE)
    created_date   = models.DateTimeField(auto_now_add=True)
    modified_date  = models.DateTimeField(auto_now_add=True)
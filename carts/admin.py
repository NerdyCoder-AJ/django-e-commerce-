from store.models import Product
from django.contrib import admin
from .models import Cart, CartItem

admin.site.register(Cart)

class CartItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(CartItem, CartItemAdmin)


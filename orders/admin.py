from django.contrib import admin
from .models import Order, OrderProduct, Payment
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name' , 'phone', 'email', 'city', 'state','order_total','gst', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'phone', 'email']
    list_per_page = 20

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_id', 'payment_method', 'amount_paid', 'status', 'created_at']
    list_filter = ['payment_id',]
    search_fields = ['payment_id',]
    list_per_page = 20

    
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'product_price', 'ordered', 'creted_at']
    list_per_page = 20

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)


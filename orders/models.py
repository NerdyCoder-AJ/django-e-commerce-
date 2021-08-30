from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import Account
from store.models import Product, Variation

class Payment(models.Model):
    user           = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id     = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid    = models.CharField(max_length=100)
    status         = models.CharField(max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.payment_id

class Order(models.Model):

    STATUS = (
        ('NEW', 'NEW'),
        ('ACCEPTED', 'ACCEPTED'),
        ('COMPLETED', 'COMPLETED'),
        ('CANCELLED', 'CANCELLED'),
    )

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_total = models.FloatField()
    gst = models.FloatField()
    status = models.CharField(choices=STATUS, max_length=10, default='NEW')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f'{self.first_name}  {self.last_name}'
    
    def full_address(self):
        return f'{self.address_line_1}  {self.address_line_2}'

    def __str__(self):
        return self.first_name 


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)  
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField()
    product_price = models.IntegerField()
    ordered = models.BooleanField(default=False)
    creted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order

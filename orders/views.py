from django.shortcuts import redirect, render
from carts.models import CartItem
from .forms import OrderForm
from .models import Order, Payment
import uuid
import datetime
import json

def payments(request):
    body = json.loads(request.body)
    print(body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])
    payment = Payment(
        user = request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount_paid = order.order_total,
        status = body['status'],
    )
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.save()
    return render(request, 'orders/payments.html')


def place_order(request, total=0, quantity=0):
    current_user = request.user

    cart_items = CartItem.objects.filter(is_active=True)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store-page')

    grand_total = 0
    gst = 0
    for cart_item in cart_items:
         total += (cart_item.product.price * cart_item.quantity)
         quantity += cart_item.quantity
    gst = (5 * total)/100
    grand_total = (total + gst)

    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.pincode = form.cleaned_data['pincode']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.country = form.cleaned_data['country']
            data.order_total = grand_total
            data.gst = gst
            data.ip = request.META.get('REMOTE_ADDR')

            # Genrate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            order_numbers = current_date + str(uuid.uuid4())
            data.order_number = order_numbers

            data.save()
            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_numbers)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'grand_total': grand_total,
                'gst': gst
            }
            return render(request, 'orders/payments.html', context)
    else:
        return redirect('checkout')
    

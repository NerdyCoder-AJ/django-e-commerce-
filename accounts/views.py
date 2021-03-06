from decimal import Context
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Account
from orders.models import Order, OrderProduct

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            return redirect('dashboard')
        else:
            messages.warning(request, 'email and password is incorrect')
            return redirect('login-page')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.save()

            # account verification
            current_site = get_current_site(request)
            mail_subject = 'Plese verify your email'
            message = render_to_string('accounts/account_verification.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
             
            messages.success(request, 'We have sent you verification email to your email address. please verify it')
            return redirect('register')
    else:
        form = RegistrationForm()
 
    context = {

        'form': form
    }
    return render(request, 'accounts/register.html', context)



def logout(request):
    auth.logout(request)
    return redirect('login-page')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Cogratulations! Your account is activated.')
        return redirect('login-page')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')

        
@login_required(login_url='login-page')
def dashboard(request):
    orders = Order.objects.filter(user=request.user, is_ordered = True)
    order_count = orders.count()
    context = {
        'order_count': order_count
    }
    return render(request, 'accounts/dashboard.html', context)


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            #  Reset password email 
            current_site = get_current_site(request)
            mail_subject = 'Reset your email'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
             
            messages.success(request, 'Password reset email sent to your email address')
            return redirect('login-page')
        else:
            messages.error(request, 'Account does not exists')
            return redirect('forgotpassword')

    return render(request, 'accounts/forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'plese reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expipred')
        return redirect('login-page')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'password reset succesful')
            return redirect('login-page')
        else:
            messages.error(request, 'password do not match')
            return redirect(request, 'resetPassword')
    else: 
       return render(request, 'accounts/resetPassword.html')


@login_required(login_url='login-page')
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered = True).order_by('-created_at')
    context = {
        'orders': orders
    }
    return render(request, 'accounts/my_orders.html', context)


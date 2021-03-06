from django import views
from django.urls import path
from . import views
urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login-page'),
    path('logout/', views.logout, name='log_out'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    
    path('my_orders/', views.my_orders, name='my_orders'),

]
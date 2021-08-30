from django import views
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.StoreViewPage, name='store'),
    path('category/<slug:category_slug>/', views.StoreViewPage, name='product-by-category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.ProductDetailPage, name='product-detail'),
    path('search/', views.search, name='search')
]
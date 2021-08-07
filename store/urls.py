from django import views
from django.urls import path
from .views import StoreViewPage, ProductDetailPage 
urlpatterns = [
    path('', StoreViewPage, name='store-page'),
    path('<slug:category_slug>/', StoreViewPage, name='product-by-category'),
    path('<slug:category_slug>/<slug:product_slug>/', ProductDetailPage.as_view(), name='product-detail')
]
from django.shortcuts import render
from django.views import generic 
from store.models import Product

class HomePageView(generic.ListView):
    template_name    = 'webpages/home.html'
    queryset = Product.objects.all().filter(is_available=True)
    context_object_name = 'products'
    
    
    

    



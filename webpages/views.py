from django.shortcuts import render
from django.views import generic 
from store.models import Product

class HomePageView(generic.TemplateView):
    template_name    = 'webpages/home.html'


    def products(self):
        return Product.objects.all().filter(is_available=True, is_popular=True)

    # queryset = Product.objects.all().filter(is_available=True, is_popular=True)
    # context_object_name = 'products'
    
    
    

    



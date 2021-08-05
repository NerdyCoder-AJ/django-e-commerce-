from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Product
from category.models import Category


class StoreViewPage(generic.TemplateView):
    template_name = 'store/store.html'

    def get_context_data(self, category_slug=None, **kwargs):
        context = super(StoreViewPage, self).get_context_data(**kwargs)

        categories = None
        products = None
        if category_slug is not None:
            categories = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.all().filter(category=categories, is_available=True)
            product_count = Product.objects.filter(
                category=categories, is_available=True).count()
        else:
            products = Product.objects.all().filter(is_available=True)
            product_count = Product.objects.all().filter(is_available=True).count()

        context.update({
            'products': products,
            'product_count': product_count
        })
        return context


class ProductDetailPage(generic.TemplateView):
    template_name = 'store/product_detail.html'

    def get_context_data(self, category_slug, product_slug=None, **kwargs):
        context = super(ProductDetailPage,  self).get_context_data(**kwargs)

        try:
            single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        except Exception as e:
            raise e

        context.update({
            'single_product': single_product
        })
        return context

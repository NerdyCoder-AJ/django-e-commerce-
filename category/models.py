from django.db import models

# Category Model
class Category(models.Model):
    category_name  = models.CharField(max_length=100, unique=True)
    slug           = models.SlugField(max_length=100, unique=True)
    description    = models.TextField(max_length=255, blank=True)
    cat_img        = models.ImageField(upload_to='media/category')
    created_date   = models.DateTimeField(auto_now_add=True)
    
    # plural name for admin panel
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
        
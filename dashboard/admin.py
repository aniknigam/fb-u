from django.contrib import admin
from .models import Product # . means current directory

# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'seller_name', 'seller_phone', 'price', 'featured_product')
    ordering = ('product_name',)
    search_fields = ('product_name', 'seller_name', 'seller_phone')
    list_filter = ('product_name', 'price', 'pub_date', 'featured_product')


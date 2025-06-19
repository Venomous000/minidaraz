from django.contrib import admin
from .models import Product, Category, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price_per_piece', 'stock_quantity', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('product_name',)
    inlines = [ProductImageInline]


admin.site.register(Category)

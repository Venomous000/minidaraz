# Register your models here.
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_amount', 'is_paid')
    list_filter = ('is_paid', 'order_date')
    search_fields = ('user__email',)
    inlines = [OrderItemInline]


admin.site.register(OrderItem)

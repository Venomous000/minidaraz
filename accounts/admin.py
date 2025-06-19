# Register your models here.
from django.contrib import admin
from .models import User, Admin, Address
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'name')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )


admin.site.register(Admin)
admin.site.register(Address)

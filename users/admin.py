from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)

    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'country', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация',
         {'fields': ('phone_number', 'country', 'avatar')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
       (None, {'fields': ('phone_number', 'country', 'avatar')})
    )
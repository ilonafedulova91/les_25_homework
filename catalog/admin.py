from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "purchase_price", "category", "id")
    list_filter = ("category",)
    search_fields = ("name", "description")

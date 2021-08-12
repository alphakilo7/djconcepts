from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "tagline", "price")
    search_fields = ["title", "tagline"]


# Register your models here.
admin.site.register(Product, ProductAdmin)

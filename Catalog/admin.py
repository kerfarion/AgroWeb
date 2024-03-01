from django.contrib import admin
from .models import Category, Kind, Product


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", ]
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "category"]
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "stock", "available", "created", "updated", ]
    list_filter = ["available", "created", "updated", "stock", "kind"]
    list_editable = ["price", "stock", "available"]
    prepopulated_fields = {"slug": ("name", )}

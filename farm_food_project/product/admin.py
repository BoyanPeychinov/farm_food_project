from django.contrib import admin

from farm_food_project.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

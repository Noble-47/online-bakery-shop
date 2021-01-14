from django.contrib import admin

from.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created', 'updated', 'get_absolute_url', 'category']
    list_filter = ['created', 'updated']
    list_editable = ['price', 'category']
    prepopulated_fields = {'slug': ('name',)}    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

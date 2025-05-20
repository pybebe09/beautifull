from django.contrib import admin
from .models import Product,About,Client
# Register your models here.
admin.site.register(About)
admin.site.register(Client)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("name",)}


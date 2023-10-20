from django.contrib import admin
from .models import Category, Product, Order, Client

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)


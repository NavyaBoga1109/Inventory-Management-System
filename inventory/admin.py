from django.contrib import admin
from .models import Supplier, Product, SaleOrder

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(SaleOrder)

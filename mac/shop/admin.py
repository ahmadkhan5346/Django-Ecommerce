from django.contrib import admin

# Register your models here.
from.models import OrderUpdate, Product, Contact, Orders
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)


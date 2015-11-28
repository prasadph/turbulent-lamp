from django.contrib import admin
from .models import Food, Detail, Order, Customer
# Register your models here.

admin.site.register(Food)
admin.site.register(Detail)
admin.site.register(Customer)
admin.site.register(Order)

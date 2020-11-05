from django.contrib import admin

from .models import CustomUser, Order, MenuItem, LineItem

admin.site.register(CustomUser)
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(LineItem)

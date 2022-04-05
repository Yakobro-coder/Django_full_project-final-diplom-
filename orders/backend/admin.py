from django.contrib import admin
from .models import Users, Contacts, Shops, Categories, Products, ProductsInfo, Parameters, \
    ProductParameter, Orders, OrderItems, ConfirmEmailToken

admin.site.register(Users)
admin.site.register(Contacts)
admin.site.register(Shops)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(ProductsInfo)
admin.site.register(Parameters)
admin.site.register(ProductParameter)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(ConfirmEmailToken)

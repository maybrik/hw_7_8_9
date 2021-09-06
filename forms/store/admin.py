from django.contrib import admin

from .models import Destination, Product, Contractor, Client

admin.site.register(Destination)
admin.site.register(Product)
admin.site.register(Contractor)
admin.site.register(Client)

from django.contrib import admin
from .models import site, iap, switch,order
# Register your models here.

admin.site.register(site)
admin.site.register(iap)
admin.site.register(switch)
admin.site.register(order)

from django.contrib import admin

from .models import data


# Register your models here.
class ScripsData(admin.ModelAdmin):
    list_display = ['number', 'password', 'username', 'plane', 'customer_ip',  'time_add', 'add_date' , 'nationalId']
    search_fields = ['number']


admin.site.register(data, ScripsData)

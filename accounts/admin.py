from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Profile , UserPhoneNumber




admin.site.register(Profile)
#admin.site.register(UserAddress)
admin.site.register(UserPhoneNumber)
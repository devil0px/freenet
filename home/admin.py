from django.contrib import admin
from .models import Number


# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'created_by', 'created', 'messages_send' ,'total_msgs']
    list_filter = ['created', 'created_by', 'messages_send']
    search_fields  = ['phone_number']


admin.site.register(Number, PostsAdmin)

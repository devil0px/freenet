from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff','num_messages', 'total_msg_send', 'date_joined'
        )
    list_editable =[ 'num_messages' ,'total_msg_send']

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('num_messages','total_msg_send',)}),
)

admin.site.register(CustomUser, CustomUserAdmin)
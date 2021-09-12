from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    list_editable = ('is_active',)
    ordering = ('date_joined',)

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

class UserProfileAdmin(admin.ModelAdmin):
    def ProfilePhoto(self, object):
       return format_html('<img src="{} "width="50" style="border-radius:50%;">'.format(object.profile_picture.url))
    list_display = ['ProfilePhoto', 'user', 'pincode', 'city', 'state', 'country']

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


   
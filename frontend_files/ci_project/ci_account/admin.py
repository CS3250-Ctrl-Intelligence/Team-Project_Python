from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from ci_account.models import Account,UserProfile


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','is_admin','is_active','is_staff','is_superadmin','last_login','date_joined')

    readonly_fields = ('last_login','date_joined')
    filter_horizontal = ()
    list_filter=()
    fieldsets=()

class UserProfileAdmin(admin.ModelAdmin):

    def thumbnail(self,object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile picture'    

    list_display=('thumbnail','user','address','city','state','zip')


admin.site.register(Account,AccountAdmin)
admin.site.unregister(Group)
admin.site.register(UserProfile,UserProfileAdmin)

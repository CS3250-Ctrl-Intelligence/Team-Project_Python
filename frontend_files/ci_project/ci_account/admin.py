from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from ci_account.models import Account


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','is_admin','is_active','is_staff','is_superadmin','last_login','date_joined')

    readonly_fields = ('last_login','date_joined')
    filter_horizontal = ()
    list_filter=()
    fieldsets=()

admin.site.register(Account,AccountAdmin)
admin.site.unregister(Group)

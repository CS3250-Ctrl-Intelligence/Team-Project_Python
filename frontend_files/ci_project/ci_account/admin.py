from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ci_account.models import Account


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','email','last_login','date_joined','is_active')

    readonly_fields = ('last_login','date_joined')
    filter_horizontal = ()
    list_filter=()
    fieldsets=()

admin.site.register(Account,AccountAdmin)


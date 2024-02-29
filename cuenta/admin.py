from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cuenta.models import Cuenta

class AccountAdmin (UserAdmin):
    list_display=('email', 'username')
    search_fields=('email', 'username')
    readonly_fields= ()

    filter_horizontal= ()
    list_filter= ()
    fieldsets= ()


admin.site.register(Cuenta, AccountAdmin)
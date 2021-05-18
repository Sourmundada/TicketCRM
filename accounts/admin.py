from django.contrib import admin
from .models import Account, Staff
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', )
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    search_fields = ('email', )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

admin.site.register(Staff, AccountAdmin)


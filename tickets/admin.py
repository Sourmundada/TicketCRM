from django.contrib import admin

from .models import Ticket, Attachment

class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'assigned_to', 'status')
    search_fields = ('name', 'description',)
    list_editable = ('status',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Attachment)
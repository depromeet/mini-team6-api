from django.contrib import admin

from .models import Party, Billing


class PartyAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        'title',
        'total',
        'date',
    ]


admin.site.register(Party, PartyAdmin)
admin.site.register(Billing)

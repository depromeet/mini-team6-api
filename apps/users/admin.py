from django.contrib import admin

from .models import MyUser


class UseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'username',
        'provider',
        'email',
        'phone',
        'is_active',
        'is_admin',
    ]
    fieldsets = (
        (None, {
            'fields': ('username', 'name', 'email', 'phone'),
        }),
        ('추가 정보', {
            'fields': ('provider', 'uid', 'is_active', 'is_admin', 'date_joined'),
        })
    )
    readonly_fields = ['date_joined']


admin.site.register(MyUser, UseAdmin)

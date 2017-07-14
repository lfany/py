from django.contrib import admin

from .models import TestModel, Contact, Tag


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


admin.site.register([TestModel, Tag])
admin.site.register(Contact, ContactAdmin)

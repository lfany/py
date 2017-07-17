from django.contrib import admin

from .models import TestModel, Contact, Tag


# Register your models here.


class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)  # search
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


admin.site.register([TestModel])
admin.site.register(Contact, ContactAdmin)

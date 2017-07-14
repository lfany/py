from django.contrib import admin

from .models import TestModel, Contact, Tag


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')


admin.site.register([TestModel, Tag])
admin.site.register(Contact, ContactAdmin)

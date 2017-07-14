from django.contrib import admin

from .models import TestModel, Contact, Tag

# Register your models here.

admin.site.register([TestModel, Contact, Tag])

from django.contrib import admin

# Register your models here.

from .models import Person,Pc_assets

admin.site.register(Person)
admin.site.register(Pc_assets)
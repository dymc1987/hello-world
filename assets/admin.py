from django.contrib import admin

# Register your models here.

from .models import Person,Pc_assets

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'job_position')
    search_fields = ('name', 'department', 'job_position')
    list_editable = ('name', 'department', 'job_position')
    list_display_links = None

class Pc_assetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pc_type', 'sn', 'assets_num')
    search_fields = ('pc_type', 'sn', 'assets_num')
    list_editable = ('pc_type', 'sn')
    list_display_links = None

admin.site.register(Person, PersonAdmin)
admin.site.register(Pc_assets, Pc_assetsAdmin)
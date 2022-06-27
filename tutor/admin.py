from django.contrib import admin
from tutor.models import Region, City

@admin.register(Region)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'short_name']
    list_display_links = ['id','name', 'short_name']
    list_search = ['id', 'name', 'short_name']


@admin.register(City)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']
    list_display_links = ['id','name', 'region']
    list_search = ['id', 'name', 'region']
    list_filter = ['region']
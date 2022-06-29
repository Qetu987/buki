from django.contrib import admin
from tutor.models import Region, City, Tutor

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

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'city', 'is_active']
    list_display_links = ['id','first_name', 'last_name', 'city']
    list_search = ['id', 'first_name', 'last_name', 'email']
    list_filter = ['is_active', 'city']
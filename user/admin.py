from django.contrib import admin
from user.models import User, Mark

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'city', 'is_active']
    list_display_links = ['id','first_name', 'last_name', 'email']
    list_search = ['id', 'city', 'email', 'first_name', 'last_name']
    list_filter = ['city', 'is_active']

    
@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'tutor', 'mark', 'created']
    list_display_links = ['id','student', 'tutor', 'mark']
    list_search = ['id', 'student', 'tutor', 'mark']
    list_filter = ['mark', 'tutor']
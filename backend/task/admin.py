from django.contrib import admin
from .models import Task, Profile
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'concluded')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(Task, TaskAdmin)
admin.site.register(Profile, ProfileAdmin)
from django.contrib import admin
from .models import Department, Task, Profile


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'deadline', 'status', 'created_by']
    list_filter = ['status', 'department']
    search_fields = ['title', 'description']
    list_editable = ['status']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'is_manager']
    list_filter = ['is_manager', 'department']
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'email', 'gender', 'age', 'interest', 'course', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('gender', 'course', 'created_at')
    ordering = ('-created_at',)

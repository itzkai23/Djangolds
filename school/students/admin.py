from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'email', 'gender', 'age', 'interest', 'course')
    search_fields = ('first_name', 'last_name', 'email')
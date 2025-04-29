from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'address', 'email', 'gender', 'age', 'interest']
        # ⚡ No need for 'course' field in the form anymore

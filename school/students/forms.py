from django import forms
from .models import Student
# from .models import Post

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'address', 'email', 'gender', 'age', 'interest']
        # ⚡ No need for 'course' field in the form anymore

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'interest': forms.Textarea(attrs={'class': 'form-control'}),
        }

# class PostForm(forms.ModelForm):
#     class Meta: 
#         model = Post
#         fields = ('title', 'title_tag', 'author', 'body')

#         widget = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.TextInput(attrs={'class': 'form-control'}),
#             'body': forms.TextInput(attrs={'class': 'form-control'}),
#         }
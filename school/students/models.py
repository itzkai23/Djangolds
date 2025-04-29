from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(default="Pampano St, Maya-Maya St, Malabon, Metro Manila")
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )
    interest = models.TextField(max_length=50, default=" ")
    course = models.TextField(max_length=50, blank=True)  # ✅ Allow course to be blank initially
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

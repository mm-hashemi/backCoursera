from django.contrib.auth.models import AbstractUser
from django.db import models
from courses.models import Purchase,Course
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Instructor', 'Instructor'),
        ('Admin', 'Admin'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Suspended', 'Suspended'),
        ('Banned', 'Banned'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course, blank=True,related_name='profiles')
    profile = models.ImageField(upload_to='profile/', blank=True, null=True)

    REQUIRED_FIELDS = ['email']
    # USERNAME_FIELD = 'username'  # or 'email' if you want login with email

    def __str__(self):
        return self.email

    @property
    def enrolled_courses(self):
        return Purchase.objects.filter(user=self.id).count()

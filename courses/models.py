from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    salary=models.IntegerField(default=0)
    credentials=models.CharField(max_length=50)
    image=models.ImageField(upload_to='roles/')
    category=models.CharField(max_length=50)
    startDate=models.CharField(max_length=50)

    @property
    def students_count(self):
        # Count how many purchases are associated with this course
        return self.purchase_set.count()  # 'purchase_set' is the reverse relation by default

    def __str__(self):
        return self.title


   

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='purchases')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    bought_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # ✅ correct here

    def __str__(self):
        return f"{self.user.username} bought {self.course.title}"

class HeroBanner(models.Model):
    banner=models.ImageField(upload_to='banner/', blank=True, null=True)
    description=models.CharField(max_length=70)

class Companies(models.Model):
    logoImage=models.ImageField(upload_to='companies/', blank=True, null=True)

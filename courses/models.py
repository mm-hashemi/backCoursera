from django.db import models

# Create your models here.
class Role(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    salary=models.IntegerField(default=0)
    credentials=models.CharField(max_length=50)
    image=models.ImageField(upload_to='roles/')
    category=models.CharField(max_length=50)
    startDate=models.CharField(max_length=50)

class HeroBanner(models.Model):
    banner=models.ImageField(upload_to='banner/')
    description=models.CharField(max_length=70)

class Companies(models.Model):
    logoImage=models.ImageField(upload_to='companies/')

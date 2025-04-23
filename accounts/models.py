from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class User(models.Model):
    email= models.EmailField((""), max_length=254,unique=True)
    password = models.CharField()



    def save(self, *args, **kwargs):
        # Hash password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.email
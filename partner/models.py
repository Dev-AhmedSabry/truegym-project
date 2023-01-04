from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Partner(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='partner/', blank=True)

    def __str__(self):
        return self.name

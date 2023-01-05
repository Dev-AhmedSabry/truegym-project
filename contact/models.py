from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=11)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class OurTeam(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    about = models.TextField(max_length=500)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='contact/', null=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    pass
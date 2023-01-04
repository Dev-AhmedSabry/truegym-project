from django.db import models
from django.contrib.auth.models import User


# Create your models here.


CITY_CHOICES = (
    ('Cairo','Cairo'),
    ('Giza','Giza'),
)

AREA_CHOICES = (
    ('NC','Nasr City'),
    ('MA','Maadi'),
    ('DK','Doki'),
    ('HR','Haram'),
    ('FS','Faisal'),
    ('OC','6 October'),
)

SUPSCRIPTION_TYPE = (
    ('D','Daily'),
    ('W','Weekly'),
    ('M','Monthly'),
    ('3 M','3 Months'),
    ('6 M','6 Months'),
    ('Y','Yearly'),
)

GENDER_CHOICES = (
    ('B','Both'),
    ('M','Male'),
    ('F','Female'),
)

RATING_CHOICES =(
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Gym(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=254, blank=True, default='')
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    area = models.CharField(max_length=30, choices=AREA_CHOICES)
    address = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=11, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='gym/', blank=True, default='')
    review = models.CharField(max_length=2, choices=RATING_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # is_email_verified = models.BooleanField(default=False)
    # is_phone_verified = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

        


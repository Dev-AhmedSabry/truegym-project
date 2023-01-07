from django.db import models
from django.contrib.auth.models import User


# Create your models here.


CITY_CHOICES = (
    ('cairo','Cairo'),
    ('giza','Giza'),
)

AREA_CHOICES = (
    ('nasr-city','Nasr City'),
    ('maadi','Maadi'),
    ('doki','Doki'),
    ('haram','Haram'),
    ('faisal','Faisal'),
    ('6-october','6 October'),
)

SUPSCRIPTION_TYPE = (
    ('daily','Daily'),
    ('weekly','Weekly'),
    ('monthly','Monthly'),
    ('3-months','3 Months'),
    ('6-months','6 Months'),
    ('yearly','Yearly'),
)

GENDER_CHOICES = (
    ('both','Both'),
    ('male','Male'),
    ('female','Female'),
)

RATING_CHOICES =(
    (1, '1 Star'),
    (2, '2 Stars'),
    (3, '3 Stars'),
    (4, '4 Stars'),
    (5, '5 Stars'),
)

class Gym(models.Model):
    
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=254, blank=True, default='')
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    area = models.CharField(max_length=30, choices=AREA_CHOICES)
    address = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=11, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='gym/', blank=True, default='')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    review = models.CharField(max_length=2, choices=RATING_CHOICES, null=True)
    # is_email_verified = models.BooleanField(default=False)
    # is_phone_verified = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

        


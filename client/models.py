from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField


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

# USER_TYPE_CHOICES = (
#         (1, 'client'),
#         (2, 'gym'),
#         (3, 'partner'),
#         (4, 'staff'),
#         (5, 'admin'),
#     )

GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
    )

# class Area(models.Model):

#     area = models.CharField(max_length=50, choices=AREA_CHOICES)
    
#     def __str__(self):
#         return self.area


# class City(models.Model):

#     city = models.CharField(max_length=50, choices=CITY_CHOICES)
#     area = models.ForeignKey(Area, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.city


# class Location(models.Model):

#     address = models.CharField(max_length=70, blank=True, default='')
#     location = PlainLocationField(based_fields=['address'], zoom=7)

    
class Client(models.Model):
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=20, choices=CITY_CHOICES, blank=True)
    area = models.CharField(max_length=30, choices=AREA_CHOICES, blank=True)
    address = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=11, blank=True, default='')
    avatar = models.ImageField(upload_to='client/', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    # user_type = models.PositiveBigIntegerField(choices=USER_TYPE_CHOICES)
    # is_email_verified = models.BooleanField(default=False)
    # is_mobile_verified = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)

    @property
    def full_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    def __str__(self):
        return f'{self.full_name}'  # self.full_name

    def __unicode__(self):
        return self.username if self.get_full_name() == "" else self.get_full_name()


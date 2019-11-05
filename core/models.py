from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be upto 10 digits")
    phone_no = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
   

    def __str__(self):
        return self.username




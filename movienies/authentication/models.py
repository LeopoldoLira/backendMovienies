from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    REQUIRED_FIELDS = [
        'username', 'first_name', 'last_name'
    ]

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
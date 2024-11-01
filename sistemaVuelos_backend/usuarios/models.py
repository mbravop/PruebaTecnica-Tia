from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

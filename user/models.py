from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid

class User(AbstractBaseUser):
    id= models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=25, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'


# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.contrib.auth.models import PermissionsMixin,  AbstractUser


class CustomUser(AbstractUser):
    num_messages = models.IntegerField(default=10,related_name='users.CustomUser.groups' , on_delete=models.CASCADE )
    total_msg_send = models.IntegerField(default=0)

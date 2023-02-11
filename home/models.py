from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.contrib.auth.models import PermissionsMixin,  AbstractUser
from django.conf import settings
import datetime
from django.utils.timezone import now
# Create your models here.
class Number(models.Model):
    phone_number = models.CharField(max_length=11)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='topics' ,  on_delete=models.CASCADE )
    created = models.DateTimeField(default=now, blank=True)
    messages_send = models.IntegerField(default=0)
    total_msgs = models.TextField(default='0')





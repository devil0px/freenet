from django.db import models
from django.conf import settings

# Create your models here.
class data(models.Model):
    username = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    number2 = models.CharField(max_length=200)
    time_add = models.IntegerField(default=0)
    password= models.CharField(max_length=200)
    plane = models.CharField(max_length=200)
    customer_ip = models.CharField(max_length=50)
    # user_send = models.ForeignKey(settings.AUTH_USER_MODEL ,  on_delete=models.CASCADE )
    add_date = models.DateTimeField(auto_now=True)
    nationalId = models.CharField(max_length=200)

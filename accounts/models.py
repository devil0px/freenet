from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
from utils.generate_code import generaste_code


class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name=_("user"),related_name='Profile' ,on_delete=models.CASCADE)
    image = models.ImageField(_("Profile"),upload_to='profile/',null=True,blank=True)
    code = models.CharField(_("Code"),max_length=8 ,default=generaste_code)
    code_used = models.BooleanField(_("Code Used"),default=False)

    def __str__(self):
        return self.user.username 
    

    # create user -----> crate profile 
@receiver(post_save,sender=User)       
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)        
        
        
    
DATA_TYPE=(
    ('Home','Home'),
    ('Office','Office'),
    ('Bussines','Bussines'),
    ('Academy','Academy'),
    ('Others','Others'),
)    
    
class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User,related_name='UserPhone' ,verbose_name=_("User"),on_delete=models.CASCADE)
    phone_number = models.CharField(_("Phone Number"),max_length=15)
    type = models.CharField(_("Type"),max_length=10,choices=DATA_TYPE)

    def __str__(self):
        return f"{self.user.username} - {self.type}"  
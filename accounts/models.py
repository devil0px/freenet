from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _



class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name=_("user"),related_name='Profile' ,on_delete=models.CASCADE)
    image = models.ImageField(_("Profile"),upload_to='profile/',null=True,blank=True)
    code = models.CharField(_("Code"),max_length=8 ,default=generaste_code)
    code_used = models.BooleanField(_("Code Used"),default=False)

    def __str__(self):
        return self.user.username    
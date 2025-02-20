from django.db import models
from django.contrib.auth.models import AbstractUser
from cryptography.fernet import Fernet
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings

key = b'6x_kZUE0hu1siWW00yIcJj0u6xWHNVV7k1Euia_LHQ4='
fernet=Fernet(key)
class Custom_User(AbstractUser):
 cnic=models.CharField(max_length=100)
 Phone_Number=models.CharField(max_length=13)
 
 
 def save(self,*args, **kwargs):
  self.cnic=(fernet.encrypt(self.cnic.encode())).decode()
  super().save(*args, **kwargs)
 
 
 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
 if created:
  token=Token.objects.create(user=instance)
  print(f"{token.key}:{instance}")
  

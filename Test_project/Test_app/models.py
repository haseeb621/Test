from django.db import models
from django.contrib.auth.models import AbstractUser,User

class CustomUser(models.Model):
 cnic = models.CharField(max_length=255)
 phone_number = models.CharField(max_length=15)
 
 def save(self, *args, **kwargs):
  self.cnic = self.encrypt_cnic(self.cnic)
  super(CustomUser, self).save(*args, **kwargs)

 def encrypt_cnic(self, cnic):
  encryption_dict = self.encryption_dict()
  encrypted_cnic = ''
  for char in cnic:
   encrypted_cnic += encryption_dict.get(char, char)
  return encrypted_cnic
 def decrypt_cnic(self):
  decryption_dict = self.decryption_dict()
  decrypted_cnic=''
  for char in decryption_dict:
    decrypted_cnic+=decryption_dict.get(char,char)
    return decrypted_cnic
    
def encryption_dict():
  return {
            '0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e',
            '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'
    }
  
def decryption_dict(self):
  dict=self.encryption_dict()
  decryption_dict=reverse(dict)
  return decryption_dict
  
def __str__(self):
   return f"{self.phone_number}"
 
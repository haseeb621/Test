from rest_framework import serializers
from .models import Custom_User
from cryptography.fernet import Fernet

key = b'6x_kZUE0hu1siWW00yIcJj0u6xWHNVV7k1Euia_LHQ4='
fernet = Fernet(key)

class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = Custom_User
  fields = ['username', 'password', 'cnic', 'is_staff']
    
 def to_representation(self, instance):
   data = super().to_representation(instance)
   req = self.context.get('request')
        
   print(f"Instance: {instance}")

   if req.user.is_staff:
    encrypted_cnic = data.get('cnic')
    try:
     if encrypted_cnic:
      data['cnic'] = fernet.decrypt(encrypted_cnic).decode()
     else:
      data['cnic'] = "No CNIC found"
    except Exception as e:
     data['cnic'] = "Invalid CNIC data"
   return data



    # def create(self, validated_data):
    #     if validated_data.get('cnic'):
    #         validated_data['cnic'] = fernet.encrypt(validated_data['cnic'].encode()).decode()
        
    #     user = Custom_User.objects.create_user(**validated_data)
        # return user


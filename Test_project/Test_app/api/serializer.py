from rest_framework import serializers
from Test_app.models import *

class CustomUserSerializer(serializers.ModelSerializer):
 class Meta:
  model=CustomUser
  fields='__all__'
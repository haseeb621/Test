from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
from .models import Custom_User
from rest_framework.parsers import MultiPartParser
import csv


class UserView(APIView):
 authentication_classes=[TokenAuthentication]
 permission_classes=[IsAuthenticated]
 
 def get(self,request):
  data=Custom_User.objects.all()
  serializer=UserSerializer(data,many=True,context={'request':request})
  return Response(serializer.data)   
  
class  read_csv(APIView):
 parser_classes=[MultiPartParser]
 def post(self,request):
  
  file=request.data.get('file')
  if not file:
   return Response({"error":"No file found"})
  else:
   decoded_file=file.read().decode('UTF-8').splitlines()
   print(decoded_file)
   reader = csv.reader(decoded_file)

   for row in reader:
    user_data = {
        "username": row[0],
        "password": row[1],
        "cnic": row[2],
        "Phone_Number": row[3]
     }
    
    serializer = UserSerializer(data=user_data)
    if serializer.is_valid():
     serializer.save()
    else:
     print("Invalid data:", serializer.errors)

  return Response ("User successfully added")

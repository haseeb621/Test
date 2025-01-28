from rest_framework.mixins import  CreateModelMixin
from .serializer import *
from rest_framework.generics import GenericAPIView

class StudentAPIView(
    
    CreateModelMixin,
    GenericAPIView
):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


    def post(self, request):
        return self.create(request)

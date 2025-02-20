
from django.contrib import admin
from django.urls import path,include
from Test_App.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Test_App.urls'))
]

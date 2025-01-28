
from django.contrib import admin
from django.urls import path,include
from Test_app.urls import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Test_app.urls'))
]

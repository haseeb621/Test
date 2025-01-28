from .views import *
from django.urls import path

urlpatterns = [
 path('',index,name='index'),
 path('fetch_csv',fetch_csv,name='fetch_csv'),
 path('signup_view',signup_view,name='signup_view'),
 path('login_view',login_view,name='login_view'),
 path('get_cnic',get_cnic,name='get_cnic'),
 path('logout_view',logout_view,name='logout_view'),
 
]
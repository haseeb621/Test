from django.urls import path
from .views import *
urlpatterns = [
 path('',UserView.as_view(),name='UserView'),
 path('read_csv',read_csv.as_view(),name='read_csv')
]
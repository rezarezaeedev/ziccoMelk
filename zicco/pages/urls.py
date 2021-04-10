from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='indexPage'),
    path('about', about_page, name='about_page'),
    
]
from django.urls import path
from .views import *

urlpatterns  =   [
    path('', index, name='amlak_page'),
    path('<int:melk_id>', details, name='details_page'),
    path('search', search, name='searched'),
]
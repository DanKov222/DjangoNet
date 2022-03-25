from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('<str:room_name>/', room, name='room')
]
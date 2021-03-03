from django.urls import path
from .views import *
urlpatterns=[
    path('',homepage,name='home'),
    path('questions/<int:poll_id>/',questions, name='questions'),
    path('choices/<int:questions_id>/',choices, name='choices'),
]

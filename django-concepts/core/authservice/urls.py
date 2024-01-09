from django.urls import path
from .views import *

urlpatterns = [
    path('login',login),
    path('mydetails/id=<str:id>',mydetails)
]

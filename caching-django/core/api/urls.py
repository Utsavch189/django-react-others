from django.urls import path
from .views import *
urlpatterns = [
    path('get_user/id=<int:id>',get_user)
]

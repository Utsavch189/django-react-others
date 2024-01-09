from django.urls import path
from .views import TestNormal

urlpatterns = [
path('test',TestNormal.as_view())

]
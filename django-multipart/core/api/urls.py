from django.urls import path
from .views import ApiController

urlpatterns = [
    path('',ApiController.as_view())
]

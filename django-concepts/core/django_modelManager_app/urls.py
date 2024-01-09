from django.urls import path
from .views import TestModelManager

urlpatterns = [
    path('test',TestModelManager.as_view())
]

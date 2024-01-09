from django.urls import path
from .views import TestSignals

urlpatterns = [
    path('test',TestSignals.as_view())
]

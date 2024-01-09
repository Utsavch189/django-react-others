from django.urls import re_path
from .views import *

urlpatterns = [
    re_path('register',Register.as_view()),
    re_path('login',Login.as_view()),
    re_path('test',AuthorizedTest.as_view())
]

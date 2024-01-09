from django.urls import path
from .views import MyBooksView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('mybooks/',MyBooksView.as_view()),
    path('mybooks/id=<int:id>/',MyBooksView.as_view())
]
#urlpatterns = format_suffix_patterns(urlpatterns)
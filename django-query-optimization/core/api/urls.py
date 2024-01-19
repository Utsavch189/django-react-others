from django.urls import path
from .views import (
    AuthorApiView,BookApiView
)

urlpatterns = [
    path('author/author_id=<str:author_id>/',AuthorApiView.as_view(),name="author-api-view"),
    path('book/book_id=<str:book_id>/',BookApiView.as_view(),name="book-api-view")
]

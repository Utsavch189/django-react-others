from django.urls import path
from .views import UserAPI,BrandAPI,ProductAPI,TestAPI

urlpatterns = [
    path('user/<str:id>/',UserAPI.as_view()),
    path('brand/<str:id>/',BrandAPI.as_view()),
    path('product/<str:id>/',ProductAPI.as_view()),
    path('test/',TestAPI.as_view())
]

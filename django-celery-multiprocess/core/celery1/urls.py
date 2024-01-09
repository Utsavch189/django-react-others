from django.urls import path
from .views import Test,OtpController,DynamicCeleryBeat
urlpatterns = [
    path('test',Test.as_view()),
    path('send-mail',OtpController.as_view()),
    path('set-dynamic-schedule-tasks',DynamicCeleryBeat.as_view())
]

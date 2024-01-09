
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/normal/',include('normal_app.urls')),
    path('api/v1/threading/',include('threading_app.urls')),
    path('api/v1/celery1/',include('celery1.urls'))
]

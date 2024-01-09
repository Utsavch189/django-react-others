"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/myapp/',include('myapp.urls')),
    path('api/v1/classviews/',include('classviews.urls')),
    path('api/v1/logapp/',include('logapp.urls')),
    path('api/v1/authservice/',include('authservice.urls')),
    path('api/v1/relation/',include('serializer_relation_app.urls')),
    path('api/v1/signals/',include('django_signal_app.urls')),
    path('api/v1/manager/',include('django_modelManager_app.urls')),
    path('api/v1/cookie_set_jwt/',include('cookie_set_jwt_app.urls')),
    path('api/v1/token_auth/',include('tokenbased_auth_app.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

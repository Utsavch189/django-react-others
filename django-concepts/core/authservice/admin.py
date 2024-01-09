from django.contrib import admin
from .models import MyUser,UserDetails

admin.site.register(MyUser)
admin.site.register(UserDetails)
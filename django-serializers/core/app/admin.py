from django.contrib import admin
from .models import User,Brand,Product,Test

admin.site.register(User)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Test)
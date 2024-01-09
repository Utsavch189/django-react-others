from django.contrib import admin
from .models import Author,MetaData,Book,BookMeta

admin.site.register(Author)
admin.site.register(MetaData)
admin.site.register(Book)
admin.site.register(BookMeta)
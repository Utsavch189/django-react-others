from rest_framework import serializers
from .models import MyBooks

class MyBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyBooks
        fields='__all__'
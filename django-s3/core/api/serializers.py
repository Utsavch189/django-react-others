from rest_framework import serializers
from .models import People
from django.conf import settings

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=People
        fields='__all__'
    
    def validate(self, attrs):
        uri=settings.MEDIA_URL+f'{attrs['username']}/{attrs['pic'].name}' # create uri for model's uri filed
        attrs['uri']=uri
        return super().validate(attrs)
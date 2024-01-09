from rest_framework import serializers
from .models import *

class UserSer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields='__all__'

    def create(self, validated_data):
        print(validated_data)

class ResturantSer(serializers.ModelSerializer):

    class Meta:
        model=Resturant
        fields='__all__'

    def create(self, validated_data):
        print(self.context['rest_id'])



    
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Persons
from .serializers import PersonSerializer
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL=getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)

@api_view(['GET'])
def get_user(request,id):
    if cache.get(id):
        print("in cache")
        data=cache.get(id)
    else:
        print("in db")
        q=Persons.objects.get(id=id)
        data=PersonSerializer(q).data
        cache.set(id,data)
    return Response({"data":data},status=status.HTTP_200_OK)
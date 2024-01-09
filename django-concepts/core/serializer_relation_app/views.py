from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import User,Resturant
from .serializer import UserSer,ResturantSer

def create_user(data):
    r=UserSer(data=data)
    if r.is_valid():
        r.save()
        return True
def create_resturant(data):
    r=ResturantSer(data=data)
    if r.is_valid():
        r.save()
        return True

@api_view(['POST'])
@parser_classes([JSONParser])
def craete(request):
    data=request.data
    res=create_user({
        "userid":data['userid'],
        "username":data['username']
    })
    res2=create_resturant({
        "rest_id":data['rest_id'],
        "user":User.objects.get(userid=data['userid']),
        "restname":data['restname']
    })
    return Response({"msg":"ok"},status=status.HTTP_201_CREATED)
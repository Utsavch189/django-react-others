from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from .services import Login,Details
from Auth.authorization import IsAuthorized,IsTokenValids

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        message,token=Login(username=request.data['username'],password=request.data['password'])
        if token:
            return Response({"info":message,"token":token},status=status.HTTP_200_OK)
        else:
            return Response({"info":message},status=status.HTTP_404_NOT_FOUND)
    except:
        pass


@api_view(['GET'])
@permission_classes([IsAuthorized,IsTokenValids])
def mydetails(request,id):
    try:
        details=Details(id)
        return Response({"info":details},status=status.HTTP_200_OK)
    except Exception as e:
        print(e)

from rest_framework import status
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import *

@api_view(['POST'])
@parser_classes([JSONParser])
def SaveBooks(request):
    try:
        book_name=request.data['book_name']
        price=request.data['price']
        Books.objects.create(
            name=book_name,
            price=price
        )
        return Response({"info":"book is added"},status=status.HTTP_201_CREATED)
    except:
        pass    
    return Response({"info":"server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework import status
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Person

import logging

logger=logging.getLogger('mylogger')

@api_view(['POST'])
@parser_classes([JSONParser])
def testlog(request):
    try:
        name=request.data['name']
        Person.objects.create(
            name=name
        )
        logger.info('')
        #logger.warn('h')
        return Response({"info":"person is created"},status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(getattr(e, 'message', repr(e)))   
        return Response({"info":"server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
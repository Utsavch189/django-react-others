from rest_framework.response import Response
from datetime import datetime
from rest_framework import status

def handel_exception(func):
    
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
             print('here')
             return Response({"message":str(e),"timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_400_BAD_REQUEST)
    return inner
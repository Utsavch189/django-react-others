from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
import logging

def handel_exception(log:bool=False):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                if log:
                    logger=logging.getLogger('success')
                    package=func.__module__
                    position=func.__qualname__
                    logger.info(f"package : {package} --> position : {position}")

                return func(*args, **kwargs)
            except Exception as e:
                 if log:
                    logger=logging.getLogger('error')
                    package=func.__module__
                    position=func.__qualname__
                    logger.error(f"package : {package} --> position : {position} --> exception : {str(e)}")
                    
                 return Response({"message":str(e),"timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_400_BAD_REQUEST)
        return inner
    return wrapper
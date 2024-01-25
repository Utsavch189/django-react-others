from rest_framework.views import exception_handler
from core.utils.responses.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

def get_response(exc):
    
    if isinstance(exc,APIException):
        return Response(data={"message":str(exc)},status=exc.get_codes())
    return Response(data={"message":str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    if exc:
        return get_response(exc)

    return response
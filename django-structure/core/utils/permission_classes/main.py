from rest_framework import permissions
from utils.jwt.main import JwtBuilder
from rest_framework.exceptions import APIException

class UnauthorizedException(APIException):
    status_code=401
    default_detail = {'message': 'Unauthorized'}
    default_code="Unauthorized"

class IsAuthorized(permissions.BasePermission):

    def has_permission(self,request,view):
        try:
            if request.META.get('HTTP_AUTHORIZATION'):
                access_token=request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
                if JwtBuilder(token=access_token).decode():
                    return True
            raise UnauthorizedException()
        except:
            raise UnauthorizedException()
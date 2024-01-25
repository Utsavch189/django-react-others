from rest_framework import permissions
from utils.jwt.main import JwtBuilder
from utils.exceptions.main import Unauthorized

class IsAuthorized(permissions.BasePermission):

    def has_permission(self,request,view):
        try:
            if request.META.get('HTTP_AUTHORIZATION'):
                access_token=request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
                if JwtBuilder(token=access_token).decode():
                    return True
            raise Unauthorized()
        except:
            raise Unauthorized()
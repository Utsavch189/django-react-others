from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

User=get_user_model()

class UserSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()

class Register(APIView): 
    @transaction.atomic
    def post(self,request):
        try:
            user=User(username=request.data['username'],email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            token=Token.objects.create(user=user)
            serializer=UserSerializer(user)
            return Response({
                "message":"user is created",
                "user":serializer.data,
                "token":token.key
            },status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    
    def post(self,request):
        try:
            username=request.data['username']
            password=request.data['password']
            if not User.objects.filter(username=username).exists():
                return Response({"no user found!"},status=status.HTTP_401_UNAUTHORIZED)
            
            user=User.objects.get(username=username)

            if not user.check_password(password):
                return Response({"wrong password!"},status=status.HTTP_401_UNAUTHORIZED)
            
            token,created=Token.objects.get_or_create(user=user)
            
            serializer=UserSerializer(user)
            return Response({
                "message":"logged in successfully!",
                "user":serializer.data,
                "token":token.key
            },status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class AuthorizedTest(APIView):

    authentication_classes=[SessionAuthentication,TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        try:
            return Response({"username":request.user.username},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
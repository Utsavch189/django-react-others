from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from rest_framework import serializers
import json

class BookAuthorSerializer(serializers.Serializer):
    author_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    book_name = serializers.CharField(max_length=200)
    book_price=serializers.IntegerField()

class TestModelManager(APIView):

    def get(self,request):
        try:
           author_withBooks=Author.repo_objects().get_author_withBooks('utsavchatterjee71@gmail.com')
           data=json.dumps(BookAuthorSerializer(author_withBooks,many=True).data)
           return Response({"message":"ok","data":json.loads(data)},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        try:
           pass
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request):
        try:
           pass
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request):
        try:
           pass
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
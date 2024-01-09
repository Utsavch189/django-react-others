from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SignalTest

class TestSignals(APIView):

    def post(self,request:object)->dict:
        try:
            db=SignalTest(
                name=request.data['name'],
                email=request.data['email']
            )
            db.save()
            return Response({"message":"created!","data":{
                "name":db.name,
                "email":db.email
            }},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request:object)->dict:
        try:
            obj=SignalTest.objects.get(email=request.data['email'])
            obj.name=request.data['name']
            obj.save()
            return Response({"message":"updated!"},status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
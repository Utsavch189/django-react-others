from service.db import StoreOTP
from service.email import Mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import random

class TestNormal(APIView):

    def post(self,request):
        try:
            otp=random.randint(111111,999999)
            s=StoreOTP(
                otp=otp,
                email=request.data['email']
            )
            s.store()

            m=Mail(
                subject="Test otp from django",
                body=f"OTP : {otp}",
                mail_receiver=request.data['email']
            )
            m.send()
            return Response({"message":"otp sent!"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
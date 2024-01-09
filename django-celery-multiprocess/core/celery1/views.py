from service.db import StoreOTP

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import random
from .task import test,send_mail_celery

class Test(APIView):

    def post(self,request):
        try:
            test.delay(request.data['a'],request.data['b'])
            return Response({"message":"ok!"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
class OtpController(APIView):

    def post(self,request):
        try:
            otp=random.randint(111111,999999)
            s=StoreOTP(
                otp=otp,
                email=request.data['email']
            )
            s.store()
            send_mail_celery.delay(request.data['email'],otp)
            return Response({"message":"ok!"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
        

"""
create dynamic task for celery beat 
"""
from django_celery_beat.models import PeriodicTask,CrontabSchedule
import json

class DynamicCeleryBeat(APIView):

    def post(self,request):
        try:
            schedule,created=CrontabSchedule.objects.get_or_create(hour=request.data['hour'],minute=request.data['minute'])
            tasks=PeriodicTask.objects.create(
                crontab=schedule,name=request.data['task_name'],enabled=True,task='celery1.task.schedule_mail_dynamic_to_all' ,args=json.dumps([request.data['mail_body']])
            )   
            #primary key for PerriodicTask table is 'name'                                                   
            return Response({"message":"ok!"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
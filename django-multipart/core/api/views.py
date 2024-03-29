from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PeopleSerializer
from .models import People
import base64

class ApiController(APIView):

    def get(self,request):
        try:
            people=People.objects.all()
            data=PeopleSerializer(instance=people,many=True).data
            return Response({"message":"fetched!","users":data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":e},status=status.HTTP_400_BAD_REQUEST)
        
    
    def post(self,request):
        try:
            serializer=PeopleSerializer(data=request.data)
            print(request.data) # <QueryDict: {'name': ['Sanu'], 'username': ['san87'], 'pic': [<InMemoryUploadedFile: bikess.jpg (image/jpeg)>]}>
            file=request.FILES['pic']
            """
            print(type(file))  # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
            print(type(file.read()))  # <class 'bytes'>
            print(type(str(file.read())))  # <class 'str'>

            """
                
            if serializer.is_valid():
                serializer.save()
                try:
                    base_64_encode=base64.b64encode(file.read()) # get file's base64 encoded string
                except Exception as e:
                    print(str(e))
                
                return Response({"message":"created!","user":serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(str(e))
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
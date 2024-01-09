from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import User

from .serializers import BrandSerializer
from .models import Brand

from .serializers import ProductSerializer
from .models import Product

from .serializers import TestSerializer

class TestAPI(APIView):

    def post(self,request):
        try:
            serializer=TestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
class UserAPI(APIView):

    def get(self,request,id):
        try:
            if id=='all':
                user=User.objects.all()
                serializer=UserSerializer(instance=user,many=True)

            user=User.objects.get(user_id=id)
            serializer=UserSerializer(instance=user)

            return Response({"user":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class BrandAPI(APIView):

    def post(self,request,id=None):
        try:
            serializer=BrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"brand":serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("error : ",e)
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        try:
            if id=='all':
                brand=Brand.objects.all()
                serializer=BrandSerializer(instance=brand,many=True)

            brand=Brand.objects.get(brand_id=id)
            serializer=BrandSerializer(instance=brand)

            return Response({"brand":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)

class ProductAPI(APIView):
    def get(self,request,id):
        try:
            if id=='all':
                product=Product.objects.all()
                serializer=BrandSerializer(instance=product,many=True)

            product=Product.objects.get(product_id=id)
            serializer=ProductSerializer(instance=product)

            return Response({"product":serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
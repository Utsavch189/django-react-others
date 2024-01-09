from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MyBooks
from .serializers import MyBookSerializer

class MyBooksView(APIView):
    
    def get(self,request):
        try:
            mybooks=MyBooks.objects.all()
            data=MyBookSerializer(mybooks,many=True).data
            return Response({"data":data},status=status.HTTP_200_OK)
        except:
            return Response({"data":"server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self,request):
        try:
            MyBooks.objects.create(
                book_id=request.data['book_id'],
                name=request.data['name'],
                price=request.data['price']
            )
            return Response({"data":"created","book":request.data},status=status.HTTP_201_CREATED)
        except:
            return Response({"data":"server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request,id):
        try:
            if(MyBooks.objects.filter(book_id=id).exists()):
                mybook=MyBooks.objects.get(book_id=id)

                print(mybook.discount_price(10))
                
                if (request.data.get('name') and len(request.data)==1):
                    mybook.name=request.data['name']
                elif (request.data.get('price') and len(request.data)==1):
                    mybook.price=request.data['price']
                elif (request.data.get('name') and request.data.get('price')):
                    mybook.name=request.data['name']
                    mybook.price=request.data['price']
                mybook.save()
                return Response({"data":"updated","book":{
                    'book_id':mybook.book_id,
                    'name':mybook.name,
                    'price':mybook.price
                }},status=status.HTTP_201_CREATED)
        except:
            return Response({"data":"server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request,id):
        try:
            if(MyBooks.objects.filter(book_id=id).exists()):
                MyBooks.objects.filter(book_id=id).delete()
                return Response({"data":"deleted"},status=status.HTTP_201_CREATED)
        except:
            return Response({"data":"server error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


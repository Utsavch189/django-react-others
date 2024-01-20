from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.selectors import AuthorSelector,BookSelector

class AuthorApiView(APIView):

    """
    Endpoint should be :
        /api/author/author_id=all/
            or,
        /api/author/author_id=existing_id/
    """

    def get(self,request,author_id):
        try:
            if author_id=='all':
                data=AuthorSelector.optimized_getall_author()
            else:
                data=AuthorSelector.optimized_geta_author(author_id=author_id)
            return Response({"data":data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
    


class BookApiView(APIView):

    def get(self,request,book_id):
        try:
            data=BookSelector.normal_a_book_with_its_author(book_id=book_id)
            return Response({"data":data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)
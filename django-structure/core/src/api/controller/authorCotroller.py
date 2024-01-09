from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.query_parser import query_parser
from src.api.selector.authorSelector import AuthorSelector
from src.api.service.authorService import AuthorService
from django.http import HttpResponseNotFound

class AuthorControllerApi(APIView):

    @query_parser(query_collections=[['author-id'],['page','page-size']],path='/api/v1/author')
    @handel_exception
    def get(self,request,query_dict:dict)->Response:
        message,status=AuthorSelector.get(query_dict=query_dict)
        return Response(data=message,status=status)
    
    @query_parser(query_collections=[],path='/api/v1/author')
    @handel_exception
    def post(self,request,query_dict:dict):
        message,status=AuthorService.create(data=request.data)
        return Response(data=message,status=status)

    @query_parser(query_collections=[],path='/api/v1/author')
    @handel_exception
    def put(self,request,query_dict:dict):
        message,status=AuthorService.update(data=request.data)
        return Response(data=message,status=status)

    @query_parser(query_collections=[['author-id']],path='/api/v1/author')
    @handel_exception
    def delete(self,request,query_dict:dict):
        message,status=AuthorService.delete(author_id=query_dict.get('author-id'))
        return Response(data=message,status=status)
from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.query_parser import query_parser
from src.api.selector.authorSelector import AuthorSelector
from src.api.service.authorService import AuthorService

class AuthorControllerApi(APIView):

    @query_parser(query_collections=[['author-id'],['page','page-size']],path='/api/v1/author')
    @handel_exception(log=True)
    def get(self,request)->Response:
        message,status=AuthorSelector.get(query_dict=request.query_params)
        return Response(data=message,status=status)
    
    @query_parser(query_collections=[],path='/api/v1/author')
    @handel_exception(log=True)
    def post(self,request):
        message,status=AuthorService.create(data=request.data)
        return Response(data=message,status=status)

    @query_parser(query_collections=[],path='/api/v1/author')
    @handel_exception(log=True)
    def put(self,request):
        message,status=AuthorService.update(data=request.data)
        return Response(data=message,status=status)

    @query_parser(query_collections=[['author-id']],path='/api/v1/author')
    @handel_exception(log=True)
    def delete(self,request):
        message,status=AuthorService.delete(author_id=request.query_params.get('author-id'))
        return Response(data=message,status=status)
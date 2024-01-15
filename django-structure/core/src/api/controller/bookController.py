from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorators.handelException import handel_exception
from core.utils.decorators.query_parser import query_parser
from src.api.selector.bookSelector import BookSelector
from src.api.service.bookService import BookService
from core.utils.decorators.schemaValidate import schema_validate

class BookControllerApi(APIView):

    @query_parser(query_collections=[['book-id'],['page','page-size']],path='/api/v1/book')
    @handel_exception
    def get(self,request)->Response:
        message,status=BookSelector.get(query_dict=request.query_params)
        return Response(data=message,status=status)
    
    @query_parser(query_collections=[],path='/api/v1/book')
    @schema_validate(schema_name='book_add_schema.json')
    @handel_exception
    def post(self,request):
        message,status=BookService.create(data=request.data)
        return Response(data=message,status=status)

    @query_parser(query_collections=[],path='/api/v1/book')
    @handel_exception
    def put(self,request):
        message,status=BookService.update(data=request.data)
        return Response(data=message,status=status)

    @query_parser(query_collections=[['book-id']],path='/api/v1/book')
    @handel_exception
    def delete(self,request):
        message,status=BookService.delete(book_id=request.query_params.get('book-id'))
        return Response(data=message,status=status)
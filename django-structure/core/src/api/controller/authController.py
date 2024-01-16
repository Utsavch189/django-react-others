from rest_framework.views import APIView
from core.utils.responses.response import Response
from core.utils.decorators.handelException import handel_exception
from src.api.service.authService import AuthorService
from core.utils.decorators.schemaValidate import schema_validate

class AuthControllerApi(APIView):

    @schema_validate(schema_name='login_request_schema.json')
    @handel_exception(log=True)
    def post(self,request)->Response:
        message,status=AuthorService.login(user_id=request.data.get('user_id'))
        return Response(message,status)
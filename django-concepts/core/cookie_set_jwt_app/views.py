from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .jwts import JwtBuilder
from cookie_set_jwt_app.decorator import token_creds

class Login(APIView):

    def get(self,request):
        try:
           tokens=JwtBuilder(payload={
               "sub":"utsav123"
           },access_token_exp=10,refresh_token_exp=15).get_token()
           res=Response()
           
           res.set_cookie(key='access_token',value=tokens[0]['access_token'],httponly=True,secure=True,max_age=tokens[0]['max_age'])
           res.set_cookie(key='refresh_token',value=tokens[1]['refresh_token'],httponly=True,secure=True,max_age=tokens[1]['max_age'])
           res.data={"Success" : "Login successfully","tokens":tokens}
           return res
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @token_creds
    def post(self,request,creds):
        try:
           print(creds)
           res=Response({"message":"ok"},status=status.HTTP_200_OK)
           return res
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
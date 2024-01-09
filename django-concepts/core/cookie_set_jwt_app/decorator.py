from cookie_set_jwt_app.jwts import JwtBuilder

def token_creds(func):
    def inner(self, request):
        cookie_array=request.META.get('HTTP_COOKIE').split(';')
        access_token=cookie_array[0].split('=')[1]
        refresh_token=cookie_array[1].split('=')[1]
        creds=JwtBuilder(token=access_token).decode()
        return func(self, request,creds)
    return inner
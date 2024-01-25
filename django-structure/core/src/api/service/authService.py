from rest_framework import status
from utils.jwt.main import JwtBuilder
from src.api.models import Author


class AuthorService:

    @staticmethod
    def login(user_id:str)->tuple:
        try:
            if not Author.objects.filter(user_id=user_id).exists():
                raise Exception("wrong user_id!")
            
            author=Author.objects.get(user_id=user_id)
            token_pair=JwtBuilder(
                access_token_exp=10,
                refresh_token_exp=15,
                payload={"user":user_id}
                ).get_token()
            return ({"message":"successfully logged in!","tokens":token_pair},status.HTTP_200_OK)
        except Exception as e:
            raise Exception(str(e))
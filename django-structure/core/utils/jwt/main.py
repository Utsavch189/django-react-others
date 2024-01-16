import jwt
from datetime import datetime,timedelta

class JwtBuilder:

    def __init__(self,access_token_exp:int=0,refresh_token_exp:int=0,payload:dict={},token:str="") -> None:
        self.jwt_secret:str='utsavsupratim'
        self.jwt_algos:str='HS512'
        self.access_token_exp=access_token_exp
        self.refresh_token_exp=refresh_token_exp
        self.payload=payload
        self.token=token
    
    def get_token(self)->dict:
        try:
            tokens={
                "access_token":jwt.encode(payload={**{"iat":datetime.timestamp(datetime.now()),"exp":datetime.timestamp(datetime.now()+timedelta(minutes=self.access_token_exp))},**self.payload},key=self.jwt_secret,algorithm=self.jwt_algos),
                "refresh_token":jwt.encode(payload={**{"iat":datetime.timestamp(datetime.now()),"exp":datetime.timestamp(datetime.now()+timedelta(minutes=self.access_token_exp))},**self.payload},key=self.jwt_secret,algorithm=self.jwt_algos),
            }
            return tokens
        except Exception as e:
            return False

    def decode(self) -> dict:
        try:
            return jwt.decode(self.token,self.jwt_secret,algorithms=[self.jwt_algos])
        except Exception as e:
            return False
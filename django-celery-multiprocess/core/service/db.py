from normal_app.models import OTP
from datetime import datetime,timedelta
from django.db import DatabaseError

class StoreOTP:
    def __init__(self,otp:int,email:str) -> None:
        self.otp=otp
        self.email=email

    def store(self):
        try:
            otp_obj=OTP(
                email=self.email,
                otp=self.otp,
                expires=datetime.timestamp(datetime.now()+timedelta(minutes=2))
            )
            otp_obj.save()
        except DatabaseError as e:
            raise Exception(str(e))
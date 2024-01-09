from celery import shared_task
from service.email import Mail
from .models import Mails

@shared_task
def test(a:int,b:int)->int:
    return a*b


@shared_task
def send_mail_celery(email:str,otp:int)->None:
    m=Mail(
        subject="Test otp from django",
        body=f"OTP : {otp}",
        mail_receiver=email
    )
    return m.send()

@shared_task
def schedule_mail_to_all():
    try:
        mails=Mails.objects.all()
  
        for m in mails:
         
            mail=Mail(
                subject=m.subject,
                body=m.body,
                mail_receiver=m.email
            )
            mail.send()
        return "Done"
    except Exception as e:
        print(e)


@shared_task
def schedule_mail_dynamic_to_all(self):
    try:
        mails=Mails.objects.all()
        
        print("body : ",self.request)
        for m in mails:
            
            mail=Mail(
                subject=m.subject,
                body="bodys",
                mail_receiver=m.email
            )
            mail.send()
        return "Done"
    except Exception as e:
        print(e)
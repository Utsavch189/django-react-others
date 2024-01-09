from django.core.mail import send_mail

class Mail:
    def __init__(self, subject="",body="",mail_sender="utsavpokemon9000chatterjee@gmail.com",mail_receiver=""):
        self.subject=subject
        self.body=body
        self.mail_sender=mail_sender
        self.mail_receiver=mail_receiver
    
    def send(self):
        try:
            send_mail(self.subject,self.body,self.mail_sender,[self.mail_receiver],fail_silently=False)
        except Exception as e:
            print(e)
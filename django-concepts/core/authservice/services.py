from .models import MyUser,UserDetails
from Auth.jwt import JWT_Builder

def Login(username,password):
    try:
        if (MyUser.objects.filter(username=username).exists() and MyUser.objects.get(username=username).password==password):
            tokens=JWT_Builder({"username":username}).get_token()
            message="Logged in successfully!"
            return message,tokens
        else:
            tokens=""
            message="not a existing user!"
            return message,tokens
    except Exception as e:
        print(e)

def Details(id):
    try:
        user=UserDetails.objects.get(user=id)
        return {
            'address':user.address,
            'phone':user.phone
        }
    except:
        pass
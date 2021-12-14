from django.http import HttpResponse
from .models import TOTP, TOTPLog
from .utils import tokens
from .serializers import TOTPSerializer, TOTPLogSerializer
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django_otp.util import random_hex

def index(request):
    return HttpResponse("API index")


@csrf_exempt 
def generate(request, userId):
    if request.method == 'POST':
        token_obj = tokens.TOTPVerification()
        totp_obj = TOTP.objects.create(secret=token_obj.key, userId=userId)
        print("Generated key {} for user {}".format(totp_obj.secret, str(userId)))
        return HttpResponse("Generated key {} for user {}".format(totp_obj.secret, str(userId)))
    else:
        return HttpResponse("Request method not valid")


@csrf_exempt 
def usetoken(request, userId, token):
    if request.method == 'POST':
        Totp = TOTP.objects.get(userId=userId)
        token_obj = tokens.TOTPVerification(key=Totp.secret)
        if (token_obj.verify_token(token=token)):
            log_obj = TOTPLog.objects.create(date=datetime.now(), token=token, userId=userId)
            print("Saved log on token {} for user {}".format(str(token), str(userId)))
            return HttpResponse("Saved log on token {} for user {}".format(str(token), str(userId)))
        else:
            return HttpResponse("Not verified! Try token again")
    else:
        return HttpResponse("Request method not valid")

@csrf_exempt 
def test(request):
    print(random_hex(20))
    return HttpResponse(random_hex(20))
from django.shortcuts import render,HttpResponse,render_to_response,redirect
from shandian.tools import flexihash,re
from shandian.models.models_sms import CbdSms
import time

# Create your views here.

def database(req,user_id):
    db=flexihash.getDatabase(user_id)
    return HttpResponse(db)

def sms(req,mobile):
    res=re.phone(mobile)
    if not res:
        return HttpResponse("输入的手机号码不合法")
    else:
        CbdSms.objects.using('sms').filter(tel=mobile).delete()
        CbdSms.objects.using('sms').create(tel=mobile,code='1234',createtime=time.time(),operate=35,is_send=1,sendtime=time.time(),app_resource=0)
        return HttpResponse('send message ok')

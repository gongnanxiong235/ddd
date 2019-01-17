from django.shortcuts import render,HttpResponse,render_to_response,redirect
from shandian.tools import flexihash,re
#from shandian.models.models_sms import CbdSms
from shandian.models import models,models_sms
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
        models_sms.CbdSms.objects.using('sms').filter(tel=mobile).delete()
        models_sms.CbdSms.objects.using('sms').create(tel=mobile, code='1234', createtime=time.time(), operate=35, is_send=1, sendtime=time.time(), app_resource=0)
        return HttpResponse('send message ok')


def old2new(req,user_id):
    #cbd_users
    models.CbdUsers.objects.filter(user_id=user_id).delete()
    models.CbdUsers.objects.using(flexihash.getDatabase(user_id)).filter(user_id=user_id).delete()
    #cbd_wx_users
    models.CbdWxUsers.objects.filter(user_id=user_id).delete()
    models.CbdWxUsers.objects.using(flexihash.getDatabase(user_id)).filter(user_id=user_id).delete()
    #cbd_user_access_token 只有分库有
    models.CbdUserAccessToken.objects.using(flexihash.getDatabase(user_id)).filter(user_id=user_id).delete()
    #cbd_order  分库 公共库
    models.CbdOrder.objects.filter(user_id=user_id).delete()
    models.CbdOrder.objects.using(flexihash.getDatabase(user_id)).filter(user_id=user_id).delete()
    #cbd_boost_balance
    models.CbdBoostBalance.objects.filter(user_id=user_id).delete()
    #cbd_boost_balance_change_log
    models.CbdBoostBalanceChangeLog.objects.filter(user_id=user_id).delete()
    #cbd_earn_user_reg
    models.CbdEarnUserReg.objects.filter(user_id=user_id).delete()
    #cbd_earn_account
    models.CbdEarnAccount.objects.filter(user_id=user_id).delete()
    return HttpResponse("ok")



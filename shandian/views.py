from django.shortcuts import render,HttpResponse,render_to_response,redirect
from shandian.tools import flexihash,re
#from shandian.models.models_sms import CbdSms
from shandian.models import models,models_sms,models_mongo
import time
from django.core.cache import cache

# Create your views here.

def tonew(user_id):
    # cbd_users
    models.CbdUsers.objects.filter(user_id=user_id).delete()
    models.CbdUsers.objects.using(flexihash.getDatabase(user_id)).filter(user_id=user_id).delete()
    # cbd_wx_users
    models.CbdWxUsers.objects.filter(user_id=user_id).delete()
    models.CbdWxUsers.objects.using(flexihash.getDatabase(user_id)).filter(user_id=user_id).delete()
    # cbd_user_access_token 只有分库有
    models.CbdUserAccessToken.objects.using(flexihash.getDatabase(user_id)).filter(user_id=user_id).delete()
    # cbd_order  分库 公共库
    models.CbdOrder.objects.filter(user_id=user_id).delete()
    models.CbdOrder.objects.using(flexihash.getDatabase(user_id)).filter(user_id=user_id).delete()
    # cbd_boost_balance
    models.CbdBoostBalance.objects.filter(user_id=user_id).delete()
    # cbd_boost_balance_change_log
    models.CbdBoostBalanceChangeLog.objects.filter(user_id=user_id).delete()
    # cbd_earn_user_reg
    models.CbdEarnUserReg.objects.filter(user_id=user_id).delete()
    # cbd_earn_account
    models.CbdEarnAccount.objects.filter(user_id=user_id).delete()

def index(request):
    return render(request, "shandianjj/index.html")

def database(request):
    if request.method=='POST':
        user_id=request.POST.get("user_id")
        db=flexihash.getDatabase(user_id)
        return HttpResponse(db)
    else:
        return render(request,'shandianjj/database.html')

def sendSms(request):

    if request.method=='POST':
        mobile=request.POST.get("mobile")
        print(mobile)
        res = re.phone(mobile)
        if not res:
            return HttpResponse("输入的手机号码不合法")
        else:
            models_sms.CbdSms.objects.using('sms').filter(tel=mobile).delete()
            models_sms.CbdSms.objects.using('sms').create(tel=mobile, code='1234', createtime=time.time(), operate=35, is_send=1, sendtime=time.time(), app_resource=0)
            return HttpResponse('send message ok')
    else:
        return render(request, 'shandianjj/sms.html')


def old2new(request):
    if request.method=='POST':
        user_id=request.POST.get("user_id")
        if len(user_id)==0:
            return HttpResponse("请输入user_id")
        if len(user_id)!=17:
            return HttpResponse("输入的user_id不合法,user_id是17位数字组成,请重新输入")
        tonew(user_id)
        return HttpResponse("ok")
    else:
        return render(request, 'shandianjj/old2new.html')

def old2new_mobile(request):
    if request.method=='POST':
        mobile=request.POST.get("mobile")
        res = re.phone(str(mobile).strip())
        if res:
            flag=models.CbdUsers.objects.filter(user_name=mobile).exists()
            if flag:
                user_id=str(models.CbdUsers.objects.filter(user_name=mobile)[0].user_id)
                tonew(user_id)
                return HttpResponse("ok")
            else:
                return HttpResponse("此手机号码在数据库中不存在，请检查是否正确")
        else:
            return HttpResponse("手机号码格式不正确，请检查输入是否正确")
    else:
        return HttpResponse("erro,the methed must be post method")

def setWXUsertLevel(request):
    if request.method=="POST":
        user_id=request.POST.get("user_id")
        level=request.POST.get("level")
        if len(user_id)==0:
            return HttpResponse("请输入user_id")
        if len(level)==0:
            return HttpResponse("请输入level")
        # if len(user_id)!=17:
        #     return HttpResponse("输入的user_id不合法,user_id是17位数字组成,请重新输入")
        if len(level)!=1:
            return HttpResponse("输入的level值不合法，level值由一位数字组成")
        # if user_id==None or len(user_id.strip())!=17 or level==None or len(str(level).strip())!=1:
        #     return HttpResponse("不是一个有效的user_id,请检查输入是否正确")
        # user_id=int(user_id)
        # level=int(level)
        # if user_id==None or level==None:

        qset=models_mongo.user_property.objects.filter(user_id=int(user_id))
        if len(qset)==0:
            print(11111)
            # return HttpResponse("Mongodb中不存在此user_id,请确认输入是否正确")
            models_mongo.user_property.objects.create(user_id=int(user_id),qcloud_level=int(level))
            return HttpResponse("添加并更新用户等级成功")
        else:
            user=qset[0]
            user.qcloud_level=int(level)
            user.save()
            return HttpResponse("更新用户等级成功")
    else:
        return render(request, 'shandianjj/setlevel.html')

def currentAmount(request):
    a=cache.get('boost/transfersubmit/20190130/amount_key/68830274326559136')
    print(a)
    return HttpResponse(a)


from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myset.settings")
import django
import redis
from django.core.cache import cache
from django_redis import get_redis_connection
from datetime import date
django.setup()
# Create your tests here.

if __name__ == '__main__':
    # cache.set('boost/transfersubmit/20190130/amount_key/68830274326559130',30)
    #68830274326559136

    # conn=get_redis_connection ( 'default' )  # 建立连接 default为设置的连接名
    # a=conn.get ( 'boost/transfersubmit/20190130/amount_key/68830274326559136')  # hget hash取值
    # # a = cache.get('boost/transfersubmit/20190130/amount_key/68830274326559130')
    # print(a)
    # print()str(date.today()).replace('-','')

    conn=get_redis_connection ( 'default' )  # 建立连接 default为设置的连接名
    day=str ( date.today () ).replace ( '-', '' )
    key='boost/transfersubmit/%s/amount_key/%s'

    user_id='234234'
    # amount=request.POST.get ( 'amount' )
    a=conn.get ( key % (day, user_id) )

    print ( a )
    # else:
        # return render ( request, 'shandianjj/amount.html' )
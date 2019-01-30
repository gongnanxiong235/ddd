from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myset.settings")
import django
import redis
from django.core.cache import cache
django.setup()
# Create your tests here.

if __name__ == '__main__':
    cache.set('boost/transfersubmit/20190130/amount_key/68830274326559130',30)
    #68830274326559136
    a = cache.get('boost/transfersubmit/20190130/amount_key/68830274326559130')
    print(a)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myset.settings")
import django
django.setup()
from django.test import TestCase
import datetime
from weixin import models

# Create your tests here.

if __name__ == '__main__':

    # models.Author.objects.create(name="wangwu",emali="18151143059@163.com")

    # models.Publish.objects.create(name="chinaPublish",city="shanghai")
    # models.Book.objects.create(name="python",type=1,publish_id=1)

    # 多对多添加数据
    book1=models.Book.objects.filter(id=1)[0]
    authors=models.Author.objects.all()
    book1.author.add(*authors)



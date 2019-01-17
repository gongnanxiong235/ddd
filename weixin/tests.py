import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myset.settings")
import django
django.setup()
from weixin.models.models_mytest import *

# Create your tests here.

if __name__ == '__main__':

    # models.Author.objects.create(name="wangwu",emali="18151143059@163.com")

    # models.Publish.objects.create(name="chinaPublish",city="shanghai")
    # models.Book.objects.create(name="python",type=1,publish_id=1)

    # 多对多添加数据
    # book1=models.Book.objects.filter(id=1)[0]
    # authors=models.Author.objects.all()
    # book1.author.add(*authors)

    #django的惰性机制，制定此方法的时候不会去查询数据库，用的时候再查询数据库且把对象缓存到Django自带的缓存机制中，下次再用的时候直接从缓存中取值
    #users=models.User.objects.all()
    #返回true和false，检查queryset中是否存在对象
    #print(users.exists())
    #users.update(username="zhangsan")
    #models.User.objects.create(username="wangwu",password="123456",full_name="普通员工",age=32,gender=2,role_id=2)
    #role_id大于等于2的所有对象
    #objs=models.User.objects.filter(role_id__gte=2)
    #role_id大于等于1的所有对象但排除password=123456的多有对象
    #objs=models.User.objects.filter(role_id__gte=1).exclude(password='123456')
    #full_name中包含普通的所有对象
    #objs=models.User.objects.filter(full_name__contains="普通")
    #把roleid=2的所有对象更新为roleid=3
    #models.User.objects.filter(role_id=2).update(role_id=3)
    #把queryset变成list
    # objs=models.User.objects.all()
    # print(list(objs))

    #objs=models.User.objects.values_list('role_id').distinct()
    # for i in objs:
    #     print(i)
    #models.Book.objects.create(name="PHP",type=1,publish_id=1)
    # objs=models.User.objects.raw("select *from user")
    # for i in objs:
    #     print(i.password)

    #以字典形式返回
    # def dictfetchall(cursor):
    #     "Returns all rows from a cursor as a dict"
    #     desc = cursor.description
    #     print(desc)
    #     return [
    #         dict(zip([col[0] for col in desc], row))
    #         for row in cursor.fetchall()
    #     ]
    # cursor = connection.cursor()
    #选择数据库
    #cursor = connections['my_db_alias'].cursor()
    # cursor.execute("select *from user")
    # connection.commit()
    # objs=cursor.fetchall()
    # print(objs)
    # print(dictfetchall(cursor))

    objs=Websites.objects.using("mytest").all()
    for i in objs:
        print(i)






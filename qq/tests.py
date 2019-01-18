import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myset.settings")
import django
django.setup()
from qq import model

# Create your tests here.

if __name__ == '__main__':
    # model.User.objects.using('mytest').create(name="gongnanxiong", password='111111', mobile='18151143056')
    # model.User.objects.using('mytest').create(name="gongzizun", password='111111', mobile='18151143059')
    objs = model.User.objects.all()
    for obj in objs:
        print(obj.mobile)

from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改变
'''1、在settings中的INSTALLED_APPS配置当前app，
.

2、在app中创建templatetags模块(模块名只能是templatetags)

3、在templatetags里面创建任意 .py 文件

4.在html中lode：{% load myTemplate %}'''

#过滤器 最多两个参数
@register.filter   #过滤器
def multi(x,y):
    return x*y

# {% simple_tag 参数1 参数2 ... %},不能放在if else中
@register.simple_tag
def add(a,b,c):
    return a+b+c
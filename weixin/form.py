from weixin.views import models_mytest
from django import forms
class BookForm(forms.ModelForm):
    class Meta:
        model=models_mytest.Book
        exclude=['id']
        labels = {  # 给字段添加 label
            "title": "书籍名称",
            "price": "价格"
        }
        # 自定义错误消息
        error_messages = {
            'title': {
                'max_length': '最多不能超过10个字符！',
                'min_length': '最少不能少于3个字符！'
            },
            'content': {
                'required': '必须输入content！',
            },
            'page': {
                'required': 'page参数必须字段，请传值',
                'invalid': '请输入一个可用的page参数'
            },
            'price': {
                'max_value': '图书价格不能超过1000'

            }

        }


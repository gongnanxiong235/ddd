# Generated by Django 2.1.5 on 2019-01-12 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.DeleteModel(
            name='userInfo',
        ),
    ]

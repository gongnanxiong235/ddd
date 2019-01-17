# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CbdSms(models.Model):
    sms_id = models.AutoField(primary_key=True)
    tel = models.CharField(max_length=20)
    code = models.CharField(max_length=255)
    createtime = models.IntegerField(blank=True, null=True)
    operate = models.IntegerField(blank=True, null=True)
    mobile_id = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    is_send = models.IntegerField(blank=True, null=True)
    sendtime = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)
    supplier_name = models.CharField(max_length=40, blank=True, null=True)
    supplier_account = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_sms'


class CbdSmsLog(models.Model):
    sms_id = models.IntegerField()
    err_no = models.IntegerField()
    err_msg = models.CharField(max_length=150)
    supplier_account = models.CharField(max_length=40)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_sms_log'


class CbdSmsSell(models.Model):
    sms_id = models.AutoField(primary_key=True)
    tel = models.CharField(max_length=20)
    code = models.CharField(max_length=255)
    createtime = models.IntegerField()
    operate = models.IntegerField()
    mobile_id = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    os = models.CharField(max_length=10)
    is_send = models.IntegerField()
    sendtime = models.IntegerField()
    type = models.IntegerField()
    app_resource = models.IntegerField()
    supplier_name = models.CharField(max_length=40)
    supplier_account = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'cbd_sms_sell'

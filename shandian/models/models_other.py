# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CbdUserAccessToken(models.Model):
    user_id = models.BigIntegerField()
    dev_id = models.CharField(max_length=60)
    os = models.CharField(max_length=10, blank=True, null=True)
    token = models.CharField(max_length=16)
    app_resource = models.IntegerField()
    last_update = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_access_token'
        unique_together = (('user_id', 'dev_id', 'app_resource'),)
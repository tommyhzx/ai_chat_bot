# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Process(models.Model):
    process_id = models.CharField(primary_key=True, max_length=50, db_comment='工段编号')
    process_name = models.CharField(unique=True, max_length=50, db_comment='工段名称')
    process_class = models.CharField(max_length=50, db_comment='工段类型')
    notes = models.CharField(max_length=200, blank=True, null=True, db_comment='工段描述')

    class Meta:
        managed = False
        db_table = 'process'

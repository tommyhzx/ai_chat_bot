# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProcessRoute(models.Model):
    # 工艺路线id
    route_id = models.CharField(
        primary_key=True, max_length=20, db_comment='工艺路线id')
    # 工艺路线状态
    route_status = models.CharField(
        max_length=10, blank=True, null=True, db_comment='路线状态')
    # 工艺路线名称
    route_name = models.CharField(
        unique=True, max_length=20, db_comment='工艺路线名称')
    # 步骤号
    step_number = models.IntegerField(blank=True, null=True)
    # 创建时间
    create_time = models.DateTimeField()
    # 更新时间
    update_time = models.DateTimeField()
    # 备注
    notes = models.CharField(max_length=200, blank=True,
                             null=True, db_comment='注解')
    # 版本号
    version = models.CharField(
        max_length=255, blank=True, null=True, db_comment='版本号')

    class Meta:
        managed = False
        db_table = 'process_route'

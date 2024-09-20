# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DevelopingWorkOrder(models.Model):
    process_number = models.CharField(primary_key=True, max_length=50, db_comment='数据编号(工单id-工序位置)')
    process_id = models.CharField(max_length=255, blank=True, null=True)
    work_order_number = models.ForeignKey('WorkOrder', models.DO_NOTHING, db_column='work_order_number', db_comment='工单编号')
    process_status = models.IntegerField(db_comment='工序状态（0：待开始，1：进行中，2：已暂停，3：已完成）')
    process_monitor = models.CharField(max_length=50, blank=True, null=True, db_comment='工序负责人')
    process_formula = models.JSONField(blank=True, null=True, db_comment='工艺配方')
    process_data = models.JSONField(blank=True, null=True, db_comment='工艺数据')
    start_time = models.DateTimeField(blank=True, null=True, db_comment='工序时间开始')
    end_time = models.DateTimeField(blank=True, null=True, db_comment='工序完成时间')
    notes = models.CharField(max_length=200, blank=True, null=True, db_comment='备注')
    process_material_id = models.CharField(max_length=25, blank=True, null=True, db_comment='工序物料')
    layer_name = models.CharField(max_length=25, blank=True, null=True, db_comment='层数')

    class Meta:
        managed = False
        db_table = 'developing_work_order'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProcessRouteProcessMap(models.Model):
    map_id = models.BigAutoField(primary_key=True, db_comment='主ID')
    route_id = models.CharField(max_length=255, blank=True, null=True, db_comment='工艺路线id')
    step_number = models.IntegerField(blank=True, null=True, db_comment='工序步骤号')
    process_id = models.CharField(max_length=255, blank=True, null=True, db_comment='工序id')
    formula_id = models.CharField(max_length=255, blank=True, null=True, db_comment='配方id')
    layer_name = models.CharField(max_length=255, blank=True, null=True, db_comment='层数名称')

    class Meta:
        managed = False
        db_table = 'process_route_process_map'

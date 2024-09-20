# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProcessMaterial(models.Model):
    material_id = models.CharField(primary_key=True, max_length=255, db_comment='物料id')
    material_name = models.CharField(max_length=255, blank=True, null=True, db_comment='物料名称')
    material_type = models.CharField(max_length=255, blank=True, null=True, db_comment='物料种类')
    material_code = models.CharField(max_length=255, blank=True, null=True, db_comment='物料编码')
    material_describe = models.CharField(max_length=255, blank=True, null=True, db_comment='物料描述')
    material_specification = models.CharField(max_length=255, blank=True, null=True, db_comment='物料规格')
    material_update_time = models.DateTimeField(blank=True, null=True, db_comment='更新时间')
    material_version = models.CharField(max_length=255, blank=True, null=True, db_comment='版本信息')
    material_notes = models.CharField(max_length=255, blank=True, null=True, db_comment='备注')

    class Meta:
        managed = False
        db_table = 'process_material'

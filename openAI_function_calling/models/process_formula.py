# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProcessFormula(models.Model):
    formula_id = models.CharField(primary_key=True, max_length=50, db_comment='配方id')
    process_id = models.CharField(max_length=50, blank=True, null=True, db_comment='对应工序id')
    formula_name = models.CharField(unique=True, max_length=50, db_comment='配方名称')
    formula_content = models.JSONField(blank=True, null=True, db_comment='配方内容')
    formula_status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True, null=True, db_comment='配方描述')

    class Meta:
        managed = False
        db_table = 'process_formula'

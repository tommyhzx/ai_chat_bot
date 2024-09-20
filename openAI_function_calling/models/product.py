# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='产品id')
    product_name = models.CharField(max_length=20, db_comment='产品名称')
    notes = models.CharField(max_length=500, blank=True, null=True, db_comment='产品注释')
    product_id = models.CharField(max_length=255, blank=True, null=True, db_comment='产品id')

    class Meta:
        managed = False
        db_table = 'product'

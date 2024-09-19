from django.db import models
from django.utils import timezone


class WorkOrder(models.Model):
    # 工单号
    work_order_number = models.CharField(max_length=30, unique=True)
    # 工单状态
    WORK_ORDER_STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    # 产品id
    product_id = models.CharField(max_length=30)
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now)
    # 更新时间
    update_time = models.DateTimeField(default=timezone.now)
    # 开始时间
    start_time = models.DateTimeField(default=timezone.now)
    # 结束时间
    end_time = models.DateTimeField(default=timezone.now)
    # 计划结束时间
    plan_end_time = models.DateTimeField(default=timezone.now)
    # 责任人
    principal = models.CharField(max_length=30)
    # 工艺路线id
    route_id = models.CharField(max_length=30)
    # 当前步骤
    current_step = models.CharField(max_length=30)
    # 工单数量
    quantity = models.IntegerField()
    # 备注
    work_order_notes = models.CharField(max_length=200)

    def __str__(self):
        return self.order_number

    @staticmethod
    def get_open_orders():
        return WorkOrder.objects.filter(status='open')

    @staticmethod
    def get_orders_by_date(date):
        return WorkOrder.objects.filter(created_date__date=date)

    class Meta:
        db_table = 'work_order'  # 指定数据库表名

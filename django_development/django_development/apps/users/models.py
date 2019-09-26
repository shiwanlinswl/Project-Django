from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Meta:
        db_table = 'tb_users'  # 指定数据库表名称
        verbose_name = '用户'  # 指定admin后台站点名称
        verbose_name_plural = verbose_name
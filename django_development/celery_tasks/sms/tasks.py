# 编写异步任务代码
from celery_tasks.sms.yuntongxun.sms import CCP
from . import constants
from celery_tasks.main import celery_app


@celery_app.task(name='send_sms_code')  # 用celery_app调用task方法装饰我们的函数为一个异步任务
def send_sms_code(mobile, sms_code):
    CCP().send_template_sms(mobile, [sms_code, constants.SMS_CODE_REDIS_EXPIRES // 60], 1)

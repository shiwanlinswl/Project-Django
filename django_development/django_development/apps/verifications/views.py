from django.shortcuts import render
import logging
from random import randint

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection
from . import constants
from celery_tasks.sms.tasks import send_sms_code
from celery_tasks.sms.yuntongxun.sms import CCP

# Create your views here.

logger = logging.getLogger("django")  # 创建日志输出器


class SMSCodeView(APIView):
    """
    发送短信验证码
    """
    def get(self, request, mobile):
        # 1.建立redis数据库连接
        redis_conn = get_redis_connection("verify_code")

        # # 2.查看短信标记(是否已发送过短信)
        send_flag = redis_conn.get("send_flag_%s" % mobile)

        # 3.已发送，直接响应
        if send_flag:
            return Response({"message":"短信验证已发送"}, status=status.HTTP_400_BAD_REQUEST)

        # 4.未发送，后端生成短信验证并存储验证码和标记到redis
        sms_code = "%06d" % randint(0, 999999)
        logger.debug(sms_code)
        # 创建管道
        pl = redis_conn.pipeline()
        pl.setex("sms_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        pl.setex('send_flag_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
        # 执行管道
        pl.execute()

        # 5.异步任务发送短信

        send_sms_code.delay(mobile, sms_code)

        # 6.响应
        return Response({"message":"ok"})



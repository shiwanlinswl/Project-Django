# celery启动文件(准备celery客户端)

from celery import Celery
import os
# 配置celery，如果需要用配置文件时去哪里加载
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_development.settings.dev")

# 1.创建celery客户端
celery_app = Celery('meiduo')
# 2.加载配置信息
celery_app.config_from_object('celery_tasks.config')


# 3.注册异步任务(哪些任务可以进入到任务队列)
celery_app.autodiscover_tasks(['celery_tasks.sms'])
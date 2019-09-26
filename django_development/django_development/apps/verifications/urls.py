from rest_framework.urls import url
from . import views


urlpatterns = [
    url(r"^sms_code/(?P<mobile>1[3-9]\d{9})/$", views.SMSCodeView.as_view()),  # 获取短信验证码
]
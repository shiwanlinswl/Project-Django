from rest_framework.urls import url
from . import views

patterns = [

    url(r'^users/$', views.UserView.as_view()),  # 用户注册

    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
]
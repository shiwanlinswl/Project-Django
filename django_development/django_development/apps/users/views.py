from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework.generics import CreateAPIView
from . import serializers

# Create your views here.

class UserView(CreateAPIView):
    """
    用户注册
    """
    serializer_class = serializers.UserSerializer

class UsernameCountView(APIView):
    """
    用户名数量
    """
    def get(self, request, username):
        """
        获取指定用户名数量
        """
        count = User.objects.filter(username=username).count()

        data = {
            'username': username,
            'count': count
        }

        return Response(data)


class MobileCountView(APIView):
    """
    手机号数量
    """
    def get(self, request, mobile):
        """
        获取指定手机号数量
        """
        count = User.objects.filter(mobile=mobile).count()

        data = {
            'mobile': mobile,
            'count': count
        }

        return Response(data)
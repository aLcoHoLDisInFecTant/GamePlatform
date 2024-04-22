from django.shortcuts import render

# Create your views here.
import json

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View
from django.middleware.csrf import get_token
import requests

# 接收游戏日志
def play_game(request):
    if request.method == 'POST':
        token = get_token(request)
        print("CSRF Token at registration:", token)
        # 收取json数据,并解码
        data = json.loads(request.body.decode('utf-8'))
        # 将data中的password字段加密
        data['password'] = make_password(data['password'])
        # 使用TherapistRegistrationForm表单类创建表单





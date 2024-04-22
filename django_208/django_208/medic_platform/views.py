import json

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.core import serializers
from .models import Patient
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import TherapistRegistrationForm
from django.views.generic import View
from django.middleware.csrf import get_token
import requests

# def patient_list(request):
#     # 获取所有患者记录
#     patients = Patient.objects.all()
#     # 序列化患者数据
#     data = serializers.serialize('json', patients)
#     # 返回JSON响应
#     return JsonResponse(data, safe=False)

class GetTokenView(View):
    def get(self, request):
        token = get_token(request)
        print(token)
        return JsonResponse({'status': 'success', 'res':'0', 'token': token}, status=200)

def register(request):
    if request.method == 'POST':
        token = get_token(request)
        print("CSRF Token at registration:", token)
        # 收取json数据,并解码
        data = json.loads(request.body.decode('utf-8'))
        # 将data中的password字段加密
        data['password'] = make_password(data['password'])
        # 使用TherapistRegistrationForm表单类创建表单
        form = TherapistRegistrationForm(data)
        if form.is_valid(): # 验证表单数据
            # 保存表单数据
            user = form.save()
            login(request, user)
            return JsonResponse({'status': 'success', 'message': '注册成功'}, status=200)
        # 根据姓名和用户名判断用户是否已经存在
        elif form.errors.get('username') and form.errors.get('username')[0] == 'A user with that username already exists.':
            return JsonResponse({'status': 'error', 'message': '用户名已存在'}, status=400)
        else:
            return JsonResponse({'status': 'error', 'message': '注册失败'}, status=400)
    else:
        form = TherapistRegistrationForm()
    return render(request, 'register.html', {'form': form})

def therapist_login(request):
    if request.method == 'POST':
        token = get_token(request)
        print("CSRF Token at registration:", token)
        # json解码
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        # 使用authenticate()方法验证用户
        user = authenticate(request, username=username, password=make_password(password))
        if user is not None:
            login(request, user)
            # 向前端返回重定向到home页面的响应

            return JsonResponse({'status': 'success', 'message': '登录成功'}, status=200)
        else:
            #return render(request, 'login.html', {'error': 'Invalid username or password'})
            # 待更改
            return JsonResponse({'status': 'error', 'message': '用户名或密码错误'}, status=400)
            # return redirect('register')
            # 跳转到注册页面

    else:
        return render(request, 'login.html')



'''
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    token = get_token(request)
    print("CSRF Token at registration:", token)
    #
    # patients = Patient.objects.filter(therapist=request.user)
    # return render(request, 'home.html', {'patients': patients})
    # 向前端返回信息： 包括Therapist的用户名和专业,以及其名下的患者信息
'''

def return_info_therapist(request):
    # 前端进入主页，向后端请求Therapist的信息
    # 如果用户未登录，重定向到登录页面
    if not request.user.is_authenticated:
        return redirect('login')
    # 获取当前登录的Therapist
    therapist = request.user
    # 返回Therapist的用户名和专业
    return JsonResponse({'status': 'success', 'username': therapist.username, 'major': therapist.major}, status=200)


def return_info_patient(request):
    # 前端进入主页，向后端请求Therapist的信息
    # 如果用户未登录，重定向到登录页面
    if not request.user.is_authenticated:
        return redirect('login')
    # 获取当前登录的Therapist
    therapist = request.user
    # 获取Therapist的所有患者
    patients = Patient.objects.filter(therapist=therapist)
    # 序列化患者数据
    data = serializers.serialize('json', patients)
    # 返回JSON响应
    return JsonResponse(data, safe=False)


# 取得该Therapist名下的所有游戏记录
def return_game_records(request):
    # 前端进入主页，向后端请求Therapist的信息
    # 如果用户未登录，重定向到登录页面
    if not request.user.is_authenticated:
        return redirect('login')
    # 获取当前登录的Therapist
    therapist = request.user
    # 获取Therapist的所有患者
    patients = Patient.objects.filter(therapist=therapist)
    # 序列化患者数据
    data = serializers.serialize('json', patients)
    # 返回JSON响应
    return JsonResponse(data, safe=False)

# 取得单一患者的游戏记录
def return_single_game_record(request):
    # 前端进入主页，向后端请求Therapist的信息
    # 如果用户未登录，重定向到登录页面
    if not request.user.is_authenticated:
        return redirect('login')
    # 获取当前登录的Therapist
    therapist = request.user
    # 获取Therapist的所有患者
    patients = Patient.objects.filter(therapist=therapist)
    # 序列化患者数据
    data = serializers.serialize('json', patients)
    # 返回JSON响应
    return JsonResponse(data, safe=False)
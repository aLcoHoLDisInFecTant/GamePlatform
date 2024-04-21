import json

from django.http import JsonResponse
from django.core import serializers
from .models import Patient
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import TherapistRegistrationForm
import requests

# def patient_list(request):
#     # 获取所有患者记录
#     patients = Patient.objects.all()
#     # 序列化患者数据
#     data = serializers.serialize('json', patients)
#     # 返回JSON响应
#     return JsonResponse(data, safe=False)

def register(request):
    if request.method == 'POST':
        form = TherapistRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = TherapistRegistrationForm()
    return render(request, 'register.html', {'form': form})

def therapist_login(request):
    if request.method == 'POST':
        # json解码
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        # 使用authenticate()方法验证用户
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            #return render(request, 'login.html', {'error': 'Invalid username or password'})
            return redirect('register')
            # 跳转到注册页面

    else:
        return render(request, 'login.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    patients = Patient.objects.filter(therapist=request.user)
    return render(request, 'home.html', {'patients': patients})
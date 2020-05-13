#处理请求并返回响应的函数（MVC中的C，MVT中的V）。
from django.shortcuts import render
from django.http import HttpResponse
from io import StringIO
from random import randrange

# Create your views here.

def index(request):
    fruits = ['苹果', '草莓', '榴莲', '香蕉', '葡萄', '山竹', '蓝莓', '西瓜']
    start, end = 0, randrange(len(fruits))
    ctx = {
        'greeting':'Hello, Django!',
        'num':end + 1,
        'fruits':fruits[start:end + 1]
    }

    return render(request, 'index.html', ctx)

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))
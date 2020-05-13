#!/usr/bin/pyhton3
#-*- coding:utf-8 -*-
#@Time :2020/4/26 11:48
#@File :view.py

from django.shortcuts import render
from django.http import HttpResponse

"""
def hello(request):
    context = {}
    context['hello'] = 'shengkai zhen shuai!'
    return render(request, 'hello.html', context)
"""

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))
#!/usr/bin/pyhton3
#-*- coding:utf-8 -*-
#@Time :2020/4/27 13:25
#@File :search.py

from django.http import HttpResponse
from django.shortcuts import render

#表单
def search_form(request):
    return render(request,'search_form.html')

#接收请求数据
def search(request):
    request.encodeing = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为:' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
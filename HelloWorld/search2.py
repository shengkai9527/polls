#!/usr/bin/pyhton3
#-*- coding:utf-8 -*-
#@Time :2020/4/27 13:44
#@File :search2.py

from django.shortcuts import render
from django.views.decorators import csrf

#接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
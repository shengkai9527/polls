#!/usr/bin/pyhton3
#-*- coding:utf-8 -*-
#@Time :2020/4/29 17:09
#@File :test1.py

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World"
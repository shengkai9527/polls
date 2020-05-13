from django.urls import path, include
from django.contrib import admin
from hrs import views
admin.autodiscover()

urlpatterns = [
    path('',views.index, name='index'),
]
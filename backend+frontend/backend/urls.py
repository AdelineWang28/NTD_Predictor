from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.home, name='home'),         # 原首页
    path('predict/', views.predict, name='predict'),  # 新增预测接口
]
"""brand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django import urls
from django.urls import path, include
from shop.views import home_page, new_page, cloes_page, login_page, message_page, order_page, pay_page
from django.conf.urls.static import static
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.conf import settings

def login(request):
    #指定要访问的页面，render的功能：讲请求的页面结果提交给客户端
    return render(request,'login.html')
#注册页面
def regiter(request):
    return render(request,'regiter.html')
#定义一个函数，用来保存注册的数据
def save(request):
    has_regiter = 0#用来记录当前账号是否已存在，0：不存在 1：已存在
    a = request.GET#获取get()请求
    #print(a)
    #通过get()请求获取前段提交的数据
    userName = a.get('username')
    passWord = a.get('password')
    #print(userName,passWord)
    #连接数据库
    db = pymysql.connect('127.0.0.1','root','123','db2')
    #创建游标
    cursor = db.cursor()
    #SQL语句
    sql1 = 'select * from user1'
    #执行SQL语句
    cursor.execute(sql1)
    #查询到所有的数据存储到all_users中
    all_users = cursor.fetchall()
    i = 0
    while i < len(all_users):
        if userName in all_users[i]:
            ##表示该账号已经存在
            has_regiter = 1

        i += 1
    if has_regiter == 0:
        # 将用户名与密码插入到数据库中
        sql2 = 'insert into user1(username,password) values(%s,%s)'
        cursor.execute(sql2,(userName,passWord))
        db.commit()
        cursor.close()
        db.close()
        return HttpResponse('login successful')
    else:

        cursor.close()
        db.close()
        return HttpResponse('The account already exists')

def query(request):
    a = request.GET
    userName = a.get('username')
    passWord = a.get('password')
    user_tup = (userName,passWord)
    db = pymysql.connect('127.0.0.1','root','123','db2')
    cursor = db.cursor()
    sql = 'select * from user1'
    cursor.execute(sql)
    all_users = cursor.fetchall()
    cursor.close()
    db.close()
    has_user = 0
    i = 0
    while i < len(all_users):
        if user_tup == all_users[i]:
            has_user = 1
        i += 1
    if has_user == 1:
        return HttpResponse('登录成功')
    else:
        return HttpResponse('用户名或密码有误')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls'), name="api"),
    path('', home_page, name="home"),
    path('new/',new_page, name="new"),
    path('cloes/',cloes_page, name="cloes"),
    path('login/',login_page, name="login"),
    path('message/',message_page, name="message"),
    path('order/',order_page, name="order"),
    path('pay/',pay_page, name="pay"),
    path('regiter/',regiter_page, name="pay"),


]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

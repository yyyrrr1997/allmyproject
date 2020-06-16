from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect
from hashlib import sha1
from df_user.models import *
from df_user.islogin import islogin
from df_goods.models import *
# Create your views here.
def register(request):
    context = {'title': '注册'}
    return render(request, 'df_user/register.html', context)

def register_handle(request):
    # 用户注册输入的信息
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    email = post.get('email')

    #判断两次输入的密码是否一致
    if upwd != ucpwd :
        return ('/user/register')

    # 对密码原文进行sha1的加密
    s1 = sha1()
    s1.update(upwd.encode())
    upwd2 = s1.hexdigest()
    print(upwd2)

    #将获取到的信息存入数据库
    #创建models对象，执行数据库相关操作
    user = UserInfo()
    user.uName = uname
    user.uPWD = upwd2
    user.uEmail = email
    user.save()

    # 跳转到登录页面
    return redirect('/user/login')

def register_exist(request):
    # 接收用户输入的get参数 uname
    get = request.GET
    uname = get.get('uname')
    # 在数据库中查询用户是否存在
    count = UserInfo.objects.filter(uName = uname).count()
    return JsonResponse({'count': count})

def login(request):
    uname = request.COOKIES.get('uname')
    context = {'title': '登录','error_name':0, 'error_pwd':0,'uname': uname}
    return render(request, 'df_user/login.html', context)

def login_handle(request):
    #接收用户登录输入的参数
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    remember =post.get('remember')

    # 根据用户名和密码查询数据库
    users = UserInfo.objects.filter(uName=uname)
    if len(users) > 0:
        # 用户存在
        #  对密码原文进行sha1加密
        s1 = sha1()
        s1.update(upwd.encode())
        upwd2 = s1.hexdigest()
        # 与数据库中的密文进行比较

        if upwd2 == users[0].uPWD:
            #认证成功
            # 从cookie中提取登录前保存好的路径
            url = request.COOKIES.get('url')
            red = HttpResponseRedirect(url)
            if remember:
                red.set_cookie('uname',uname)  # 记住用户名
            else:
                red.set_cookie('uname', '') # 没有记住用户名
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red

        else:
            # 登录失败
            context = {'title': '登录','error_name':0, 'error_pwd':1}
            return render(request, 'df_user/login.html', context)
    else:
        # 用户不存在
        context = {'title': '登录','error_name':1, 'error_pwd':0}
        return render(request, 'df_user/login.html', context)
@islogin
def info(request):
    # 读取数据库中的用户信息
    user = UserInfo.objects.get(id = request.session['user_id'])
    user_name = user.uName
    user_address = user.uAddress
    user_phone = user.uPhone
    context = {'title': '用户中心',
               'user_name': user_name,
               'user_address': user_address,
               'user_phone': user_phone,
               'info': 1}
    context['user_center']=1
    # 从cookies中读取最近浏览的信息
    goods_ids = request.COOKIES.get('goods_ids')
    # 判断cookies中的最近浏览商品序列是否为空
    if goods_ids and goods_ids != '':
        goods_ids = goods_ids.split(',') #以逗号为分割，转字符串为列表
    else:
        goods_ids = []
    # 注意goods_ids只保存id 我们在模板中需要名称、价格、单价、图片地址等 所以需要传递商品对象的列表
    goods_list = []
    for id in goods_ids:
        # 遍历goods_ids 根据id找到商品对象 把商品对象添加到goods_list列表中
        goods = GoodsInfo.objects.get(id = id)
        goods_list.append(goods)
    context['goods_list'] = goods_list
    return render(request, 'df_user/user_center_info.html', context)
@islogin
def order(request):
    context = {'title': '用户中心', 'order': 1}
    context['user_center'] = 1
    return render(request, 'df_user/user_center_order.html', context)
@islogin
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.uConsignee = post.get('consignee')
        user.uAddress = post.get('address')
        user.uPostcodes = post.get('postcodes')
        user.uPhone = post.get('phone')
        user.save()
    phone = user.uPhone[:3] + '****' + user.uPhone[-4:]  # 隐藏中间4个字符
    context = {'title': '用户中心',
               'site': 1,
               'uConsignee': user.uConsignee,
               'uAddress': user.uAddress,
               'uPostcodes': user.uPostcodes,
               'phone': phone
               }
    context['user_center'] = 1
    return render(request, 'df_user/user_center_site.html', context)

def logout(request):
    request.session.flush()  # 清空session缓存
    return HttpResponseRedirect('/goods') #这里选择退出登录后重定向到首页

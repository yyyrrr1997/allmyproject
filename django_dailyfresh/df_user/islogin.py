from django.http import HttpResponse, HttpResponseRedirect

def islogin(func):
    def login_func(request, *args, **kwargs):
        # 判断是否登录
        if request.session.get('user_id'):
            # 用户已经登录 可以正常访问页面
            return func(request, *args, **kwargs) #允许执行该函数
        else:
            red = HttpResponseRedirect('/user/login') # 重定向到登录页面
            path = request.get_full_path() #把原本要访问的路径保存下来
            red.set_cookie('url', path)# 把该路径存到cookie中

            # 用户未登录 跳转到登录页面
            return red
    return login_func #装饰器执行检查
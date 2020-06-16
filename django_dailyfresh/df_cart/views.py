from django.shortcuts import render
from df_cart.models import CartInfo
from django.http import JsonResponse
from df_user.islogin import islogin
# Create your views here.
@islogin
def cartindex(request):
    context={'title':'购物车',}
    uid =request.session['user_id']
    carts =CartInfo.objects.filter(user_id=uid)
    context['carts']=carts
    return render(request,'df_cart/cart.html',context)

def cartorder(request):
    context={'title':'提交订单',}
    return render(request,'df_cart/place_order.html',context)

def add(request,goodid,count):
    #从session中获取用户id
    uid=request.session.get('user_id')
    count=int(count)#字符串转整数
    #从数据库中根据用户id和商品id查询数量
    cartgood_list = CartInfo.objects.filter(user_id=uid,goods_id=goodid)
    # 对象列表cartgood_list的长度要么是0 要么是1
    if len(cartgood_list):#购物车已有该商品
        cartgood=cartgood_list[0]
        cartgood.count+=count
        cartgood.save()
    else:#购物车没有该商品
        cartgood =CartInfo()
        cartgood.user_id=uid
        cartgood.goods_id=goodid
        cartgood.count=count
        cartgood.save()
    #通过json返回购物车中商品的总数量
    result=CartInfo.objects.filter(user_id=uid).count() #求数量。相当于len()
    data={'count':result}

    return JsonResponse(data)
def edit(request, cart_id, count):
    try:
        cart = CartInfo.objects.get(id = cart_id)
        cart.count = int(count)
        cart.save()
        data = {'error': 0}
    except:
        data = {'error': 1}
    return JsonResponse(data)
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(id=cart_id)
        cart.delete()
        data = {'error': 0}
    except:
        data = {'error': 1}
    return JsonResponse(data)
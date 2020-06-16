from django.shortcuts import render
from df_goods.models import GoodsInfo, TypeInfo
from django.core.paginator import *
from df_cart.models import CartInfo
# Create your views here.
def index(request):
    print(request.session)
    fruit = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[:3]  # 最新产品 id大到小排序，选择前三个。列表。
    fruit2 = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[:4] # 热销产品 点击量gclick大到小排序，选择前四个。列表
    saltwater = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[:3]
    saltwater2 = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[:4]
    meat = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[:3]
    meat2 = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[:4]
    egg = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[:3]
    egg2 = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[:4]
    vegetable = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[:3]
    vegetable2 = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[:4]
    ice = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[:3]
    ice2 = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[:4]
    context = {'title': '首页','fruit': fruit, 'fruit2': fruit2}
    context['goods_page'] = 1
    context['saltwater'] = saltwater
    context['saltwater2'] = saltwater2
    context['meat'] = meat
    context['meat2'] = meat2
    context['egg'] = egg
    context['egg2'] = egg2
    context['vegetable'] = vegetable
    context[ 'vegetable2'] =  vegetable2
    context['ice'] = ice
    context['ice2'] =  ice2
    try:
        uid = request.session.get('user_id')
        cartcount=CartInfo.objects.filter(user_id=uid).count()
        context['cartcount'] = cartcount
    except:
        context['cartcount'] =0

    return render(request, 'df_goods/index.html', context)
def goodlist(request,typeid, pageid, sort):
    goodType = TypeInfo.objects.get(id=typeid)
    context = {'title': '商品列表',
               'sort':sort,
               'pageid':pageid,
               'typeid':typeid,
               'goodType':goodType}
    context['goods_page'] = 1
    context['goods_list'] = 1

    newtow = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')[:2]
    context['newtow'] = newtow

    sortgoods = GoodsInfo.objects.filter(gtype_id=typeid).order_by('id')
    context['sortgoods'] = sortgoods
    if sort=='2':
        sortgoods = GoodsInfo.objects.filter(gtype_id=typeid).order_by('gprice')
        context['sortgoods'] = sortgoods
    elif sort=='3':
        sortgoods = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-gclick')
    context['sortgoods'] = sortgoods

    paginator = Paginator(sortgoods, 15)  # 每页显示15个数据
    pager = paginator.page(int(pageid))  # page页
    rangepage=paginator.page_range

    context['rangepage'] = rangepage
    context['page'] = pager

    try:
        uid = request.session.get('user_id')
        cartcount=CartInfo.objects.filter(user_id=uid).count()
        context['cartcount'] = cartcount
    except:
        context['cartcount'] =0

    return render(request, 'df_goods/list.html', context)

def gooddetail(request,goodid,):
    context = {'title': '商品详情','goodid':goodid }
    context['goods_page'] = 1
    context['goods_detail'] = 1
    # 从商品id 的对象中，获取外键gtype_id 即类型id
    typeid=GoodsInfo.objects.filter(id=goodid)[0].gtype_id
    context['typeid'] = typeid
    #通过类型id 获得类型对象
    goodType = TypeInfo.objects.get(id=typeid)
    context['goodType'] = goodType
    #通过外键gtype_id 筛选出同类型的商品，按id大到小排序后取前2个
    newtow = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')[:2]
    context['newtow'] = newtow

    # 获取当前商品的对象（包含商品的所有信息）
    goodinfo=GoodsInfo.objects.get(id=goodid)
    # 增加访问量（点击量+1）
    goodinfo.gclick += 1
    goodinfo.save()
    context['goodinfo'] = goodinfo

    response=render(request, 'df_goods/detail.html', context)
    goods_ids = request.COOKIES.get( 'goods_ids')  # 5,2,7
    #  判断cookies中的商品id序列是否为空
    if goods_ids and goods_ids != '':
        # 不为空 以逗号分隔把字符串转换为列表
        goods_ids = goods_ids.split(',')
        # 如果列表中已经有当前id 则需要删除列表中原来的id
        if goodid in goods_ids:
            goods_ids.remove(goodid)
        # 把当前的id插入到列表的最前面
        goods_ids.insert(0, goodid)
        # 取前5个
        if len(goods_ids) > 5:
            goods_ids = goods_ids[:5]
    else:
        # 为空
        goods_ids = goodid
    # 使用逗号来连接列表中的每个元素
    goods_ids = ','.join(goods_ids)
    # 添加cookies信息
    response.set_cookie('goods_ids', goods_ids)

    try:
        uid = request.session.get('user_id')
        cartcount=CartInfo.objects.filter(user_id=uid).count()
        context['cartcount'] = cartcount
    except:
        context['cartcount'] =0

    return response


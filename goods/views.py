from django.shortcuts import render
from goods import models

# Create your views here.
def goods(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        goods_id = request.GET.getlist('goods_id')
        goods_name = request.GET.getlist('goods_name')
        goods_num = request.GET.getlist('goods_num')
        goods_sort = request.GET.getlist('goods_sort')
        goods_remark = request.GET.getlist('goods_remark')
        insert = models.goods.objects.create(goods_id=goods_id[0], goods_name=goods_name[0],goods_num=goods_num[0],goods_sort=goods_sort[0],goods_remark=goods_remark[0])
        insert.save()
    goods=models.goods.objects.values()
    return render(request,'goods.html',{'goods':goods})

def goods_delete(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        goods_id = request.GET.getlist('goods_id')
        deletesql = models.goods.objects.filter(goods_id=goods_id[0]).delete()
    goods=models.goods.objects.values()

    return render(request, 'goods.html',{'goods':goods})


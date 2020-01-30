from django.shortcuts import render
from out_storage import models

# Create your views here.
def out_storage(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        out_id = request.GET.getlist('out_id')
        goods_id = request.GET.getlist('goods_id')
        storage_id = request.GET.getlist('storage_id')
        subscriber_id = request.GET.getlist('subscriber_id')
        goods_price = request.GET.getlist('goods_price')
        goods_num = request.GET.getlist('goods_num')
        out_data = request.GET.getlist('out_data')
        insert = models.out_bill.objects.create(out_id=out_id[0],goods_id=goods_id[0], storage_id=storage_id[0],subscriber_id=subscriber_id[0],goods_price=goods_price[0],goods_num=goods_num[0],out_data=out_data[0])
        insert.save()
    out_bill=models.out_bill.objects.values()
    return render(request,'out_storage.html',{'out_bill':out_bill})

def out_storage_delete(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        out_id = request.GET.getlist('out_id')
        deletesql = models.out_bill.objects.filter(out_id=out_id[0]).delete()
    out_bill=models.out_bill.objects.values()

    return render(request, 'out_storage.html',{'out_bill':out_bill})

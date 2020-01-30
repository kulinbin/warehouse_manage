from django.shortcuts import render
from entry_storage import models

# Create your views here.
def entry_storage(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        entry_id = request.GET.getlist('entry_id')
        goods_id = request.GET.getlist('goods_id')
        storage_id = request.GET.getlist('storage_id')
        supplier_id = request.GET.getlist('supplier_id')
        goods_price = request.GET.getlist('goods_price')
        goods_num = request.GET.getlist('goods_num')
        entry_data = request.GET.getlist('entry_data')
        insert = models.entry_bill.objects.create(entry_id=entry_id[0],goods_id=goods_id[0], storage_id=storage_id[0],supplier_id=supplier_id[0],goods_price=goods_price[0],goods_num=goods_num[0],entry_data=entry_data[0])
        insert.save()
    entry_bill=models.entry_bill.objects.values()
    return render(request,'entry_storage.html',{'entry_bill':entry_bill})

def entry_storage_delete(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        entry_id = request.GET.getlist('entry_id')
        deletesql = models.entry_bill.objects.filter(entry_id=entry_id[0]).delete()
    entry_bill=models.entry_bill.objects.values()
    return render(request, 'entry_storage.html',{'entry_bill':entry_bill})

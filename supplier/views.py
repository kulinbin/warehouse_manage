from django.shortcuts import render
from supplier import models

# Create your views here.
def supplier(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        supplier_id = request.GET.getlist('supplier_id')
        supplier_name = request.GET.getlist('supplier_name')

        insert = models.supplier.objects.create(supplier_id=supplier_id[0], supplier_name=supplier_name[0])
        insert.save()
    supplier=models.supplier.objects.values()
    return render(request,'supplier.html',{'supplier':supplier})

def supplier_delete(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        supplier_id = request.GET.getlist('supplier_id')
        deletesql = models.supplier.objects.filter(supplier_id=supplier_id[0]).delete()
    supplier=models.supplier.objects.values()

    return render(request, 'supplier.html',{'supplier':supplier})
from django.shortcuts import render
from subscriber import models

# Create your views here.
def subscriber(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        subscriber_id = request.GET.getlist('subscriber_id')
        subscriber_name = request.GET.getlist('subscriber_name')

        insert = models.subscriber.objects.create(subscriber_id=subscriber_id[0], subscriber_name=subscriber_name[0])
        insert.save()
    subscriber=models.subscriber.objects.values()
    return render(request,'subscriber.html',{'subscriber':subscriber})

def subscriber_delete(request):
    if request.is_ajax():
        # 获取其中的某个键的值
        subscriber_id = request.GET.getlist('subscriber_id')
        deletesql = models.subscriber.objects.filter(subscriber_id=subscriber_id[0]).delete()
    subscriber=models.subscriber.objects.values()

    return render(request, 'subscriber.html',{'subscriber':subscriber})
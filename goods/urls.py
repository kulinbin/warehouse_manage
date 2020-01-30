from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^goods/', views.goods),
    url(r'^goods_delete/', views.goods_delete),
]

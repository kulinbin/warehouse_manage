from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^out_storage/', views.out_storage),
    url(r'^out_storage_delete/', views.out_storage_delete),

]

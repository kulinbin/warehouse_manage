from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^supplier/', views.supplier),
    url(r'^supplier_delete/', views.supplier_delete),
]

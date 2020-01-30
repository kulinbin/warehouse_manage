from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^entry_storage/', views.entry_storage),
    url(r'^entry_storage_delete/', views.entry_storage_delete),
]

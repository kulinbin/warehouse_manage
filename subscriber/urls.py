from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^subscriber/', views.subscriber),
    url(r'^subscriber_delete/', views.subscriber_delete),
]

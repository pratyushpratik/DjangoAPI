from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stock/(?P<pk>[\w:|-]+)/$', views.StockDetails.as_view()),

   # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name= 'detail'),
]
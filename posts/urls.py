from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_list, name='posts_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_zoom, name='post_zoom'),
    url(r'^calculadora$', views.calculadora),
    url(r'^cronometro$', views.cronometro),
    url(r'^conversor$', views.conversor),
    url(r'^chboton$', views.chboton),
]
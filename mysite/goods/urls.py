from django.conf.urls import url

from . import views

app_name = 'goods'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^roll_dice/(?P<goods_id>[0-9]+)/$', views.detail, name='detail'),
]

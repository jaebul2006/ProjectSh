from django.conf.urls import url

from . import views

app_name = 'goods'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^goods_detail/(?P<goods_id>[0-9]+)/$', views.goods_detail, name='goods_detail'),
    url(r'^roll_dice/(?P<goods_id>[0-9]+)/$', views.roll_dice, name='roll_dice'),
    url(r'^member_join/', views.member_join, name='member_join'),
]

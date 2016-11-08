from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create_poll, name='create_poll'),
    url(r'^test/$', views.test, name='test'),
]

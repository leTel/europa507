from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='home_view_url'),
    url(r'^(?P<news_id>[0-9]+)/$', views.detail_view, name='detail_view_url'),
    url(r'^add/$', views.add_view, name='add_view_url'),
]

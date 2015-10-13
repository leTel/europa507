from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.document_view, name='document_view_url'),
    url(r'^(?P<doc_id>[0-9]+)/$', views.document_detail_view, name='document_detail_view_url'),
]


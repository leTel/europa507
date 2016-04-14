from django.conf.urls import include, url
from django.contrib import admin
from e507.apps.news import views as news_views

urlpatterns = [
    # Examples:
    url(r'^$', news_views, name='home_url'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('e507.apps.news.urls', namespace='news')),
    url(r'^document/', include('e507.apps.document.urls', namespace='document')),

    url(r'^redactor/', include('redactor.urls')),
]

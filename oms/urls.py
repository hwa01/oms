from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$','omscore.views.index',name='index'),
	url(r'^omscore/','omscore.views.execute',name='execute'),
    url(r'^admin/', include(admin.site.urls)),
)

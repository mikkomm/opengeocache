from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^geocache/', include('geocache.urls', namespace='geocache')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',  'django.contrib.auth.views.login', name='login'),
	url(r'^logout/$',  'django.contrib.auth.views.logout', name='logout'),
)

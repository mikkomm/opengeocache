from django.conf.urls import patterns, url
from django.conf.urls.static import static
from geocache import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^create/$', views.GeocacheCreateView.as_view(), name='create'),
	)
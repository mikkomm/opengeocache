from django.shortcuts import get_object_or_404, render
from geocache.models import Geocache
from django.views import generic
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
	template_name = 'geocache/index.html'
	context_object_name = 'geocache_list_all'

	def get_queryset(self):
		return Geocache.objects.all().order_by('-cache_name')

class GeocacheCreateView(CreateView):
	model = Geocache
	success_url = '/geocache/'
	
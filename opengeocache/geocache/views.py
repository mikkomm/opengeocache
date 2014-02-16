from django.shortcuts import get_object_or_404, render
from geocache.models import Geocache
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import logout, authenticate, login

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoggedInMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class IndexView(generic.ListView):
	template_name = 'geocache/index.html'
	context_object_name = 'geocache_list_all'

	def get_queryset(self):
		return Geocache.objects.all().order_by('-cache_name')

class GeocacheCreateView(LoggedInMixin, CreateView):
	model = Geocache
	success_url = '/geocache/'
	fields = ['cache_name', 'cache_description', 'cache_type', 'cache_url', 'cache_secret']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(GeocacheCreateView, self).form_valid(form)
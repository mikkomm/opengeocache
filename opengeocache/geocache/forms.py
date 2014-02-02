from django.forms import Modelform
from geocache.models import Geocache

class GeocacheForm(ModelForm):
	class Meta:
		model = Geocache
		fields = ['cache_name', 'cache_description', 'cache_url', 'cache_secret']

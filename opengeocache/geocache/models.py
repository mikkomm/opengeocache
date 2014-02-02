from django.db import models

class Geocache(models.Model):
	cache_name			=	models.Charfield('Cache name', max_length=256)
	cache_description 	= 	models.Charfield('Cache description', max_length=1024)
	cache_url			=	models.Charfield('Openstreetmap URL', max_length=128)
	cache_secret		=	models.Charfield('Cache secret', max_length=128)


	status_choices		=	(
			('active','Active'),
			('inactive','Inactive')
		)

	cache_status = models.Charfield(max_length=20, choices=status_choices, default='active')

	type_choices		=	(
			('traditional', 'Traditional'),
			('micro', 'Micro'),
			('nano', 'Nano')
		)

	cache_status = models.Charfield(max_length=20, choices=type_choices, default='traditional')

	def __unicode__(self):
		return self.cache_name
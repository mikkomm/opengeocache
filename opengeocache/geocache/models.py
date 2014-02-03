from django.db import models
from django.contrib.auth.models import User

class Geocache(models.Model):
    cache_name          =   models.CharField('Cache name', max_length=256)
    cache_description   =   models.CharField('Cache description', max_length=1024)
    cache_url           =   models.CharField('Openstreetmap URL', max_length=128)
    cache_secret        =   models.CharField('Cache secret', max_length=128)
    owner               =   models.ForeignKey(User)

    status_choices      =   (
            ('active','Active'),
            ('inactive','Inactive')
        )

    cache_status = models.CharField(max_length=20, choices=status_choices, default='active')

    type_choices        =   (
            ('traditional', 'Traditional'),
            ('micro', 'Micro'),
            ('nano', 'Nano')
        )

    cache_type = models.CharField(max_length=20, choices=type_choices, default='traditional')

    def __unicode__(self):
        return self.cache_name
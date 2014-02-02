# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Geocache'
        db.create_table(u'geocache_geocache', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cache_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('cache_description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('cache_url', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('cache_secret', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('cache_status', self.gf('django.db.models.fields.CharField')(default='traditional', max_length=20)),
        ))
        db.send_create_signal(u'geocache', ['Geocache'])


    def backwards(self, orm):
        # Deleting model 'Geocache'
        db.delete_table(u'geocache_geocache')


    models = {
        u'geocache.geocache': {
            'Meta': {'object_name': 'Geocache'},
            'cache_description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'cache_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cache_secret': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'cache_status': ('django.db.models.fields.CharField', [], {'default': "'traditional'", 'max_length': '20'}),
            'cache_url': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['geocache']
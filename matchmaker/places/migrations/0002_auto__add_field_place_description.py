# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Place.description'
        db.add_column(u'places_place', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=4000, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Place.description'
        db.delete_column(u'places_place', 'description')


    models = {
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'geography': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.PlaceType']", 'null': 'True', 'blank': 'True'})
        },
        u'places.placetype': {
            'Meta': {'object_name': 'PlaceType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['places']
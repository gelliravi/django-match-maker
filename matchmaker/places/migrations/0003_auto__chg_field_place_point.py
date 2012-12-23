# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Place.point'
        db.alter_column(u'places_place', 'point', self.gf('django.contrib.gis.db.models.fields.PointField')(geography=True))

    def backwards(self, orm):

        # Changing field 'Place.point'
        db.alter_column(u'places_place', 'point', self.gf('django.contrib.gis.db.models.fields.PointField')())

    models = {
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'geography': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.PlaceType']", 'null': 'True', 'blank': 'True'})
        },
        u'places.placetype': {
            'Meta': {'object_name': 'PlaceType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['places']

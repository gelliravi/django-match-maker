# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'places_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, geography=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.PlaceType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'places', ['Place'])

        # Adding model 'PlaceType'
        db.create_table(u'places_placetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'places', ['PlaceType'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'places_place')

        # Deleting model 'PlaceType'
        db.delete_table(u'places_placetype')


    models = {
        u'places.place': {
            'Meta': {'object_name': 'Place'},
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
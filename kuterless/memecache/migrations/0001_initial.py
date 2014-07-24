# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'memecache_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('credit', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'memecache', ['Account'])

        # Adding model 'Transaction'
        db.create_table(u'memecache_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Account'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('item_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('number_of_items', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('total_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('credit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.CharField')(default=None, max_length=200)),
        ))
        db.send_create_signal(u'memecache', ['Transaction'])

        # Adding model 'Purchase'
        db.create_table(u'memecache_purchase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Transaction'])),
            ('total_price', self.gf('django.db.models.fields.IntegerField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'memecache', ['Purchase'])

        # Adding model 'Shop'
        db.create_table(u'memecache_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('segment', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['coplay.Segment'])),
            ('admin_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('currency_name', self.gf('django.db.models.fields.CharField')(default='MemeCache', max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'memecache', ['Shop'])

        # Adding model 'Product'
        db.create_table(u'memecache_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Shop'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('item_price', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('number_of_abailabale_items', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('number_of_selected_items', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('end_of_sale_at', self.gf('django.db.models.fields.DateTimeField')(default=None)),
            ('end_of_use_at', self.gf('django.db.models.fields.DateTimeField')(default=None)),
        ))
        db.send_create_signal(u'memecache', ['Product'])

        # Adding model 'Cart'
        db.create_table(u'memecache_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Shop'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('total_price', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'memecache', ['Cart'])

        # Adding unique constraint on 'Cart', fields ['shop', 'customer']
        db.create_unique(u'memecache_cart', ['shop_id', 'customer_id'])

        # Adding model 'ProductSelection'
        db.create_table(u'memecache_productselection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Product'])),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Cart'])),
            ('number_of_selected_items', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'memecache', ['ProductSelection'])

        # Adding unique constraint on 'ProductSelection', fields ['product', 'cart']
        db.create_unique(u'memecache_productselection', ['product_id', 'cart_id'])

        # Adding model 'ItemVoucher'
        db.create_table(u'memecache_itemvoucher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Shop'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Product'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('purchase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['memecache.Purchase'])),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'memecache', ['ItemVoucher'])


    def backwards(self, orm):
        # Removing unique constraint on 'ProductSelection', fields ['product', 'cart']
        db.delete_unique(u'memecache_productselection', ['product_id', 'cart_id'])

        # Removing unique constraint on 'Cart', fields ['shop', 'customer']
        db.delete_unique(u'memecache_cart', ['shop_id', 'customer_id'])

        # Deleting model 'Account'
        db.delete_table(u'memecache_account')

        # Deleting model 'Transaction'
        db.delete_table(u'memecache_transaction')

        # Deleting model 'Purchase'
        db.delete_table(u'memecache_purchase')

        # Deleting model 'Shop'
        db.delete_table(u'memecache_shop')

        # Deleting model 'Product'
        db.delete_table(u'memecache_product')

        # Deleting model 'Cart'
        db.delete_table(u'memecache_cart')

        # Deleting model 'ProductSelection'
        db.delete_table(u'memecache_productselection')

        # Deleting model 'ItemVoucher'
        db.delete_table(u'memecache_itemvoucher')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'coplay.segment': {
            'Meta': {'object_name': 'Segment'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'memecache.account': {
            'Meta': {'object_name': 'Account'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'memecache.cart': {
            'Meta': {'unique_together': "(('shop', 'customer'),)", 'object_name': 'Cart'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Shop']"}),
            'total_price': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'memecache.itemvoucher': {
            'Meta': {'object_name': 'ItemVoucher'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Product']"}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Purchase']"}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Shop']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'memecache.product': {
            'Meta': {'object_name': 'Product'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_of_sale_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            'end_of_use_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_price': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'number_of_abailabale_items': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'number_of_selected_items': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Shop']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'memecache.productselection': {
            'Meta': {'unique_together': "(('product', 'cart'),)", 'object_name': 'ProductSelection'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Cart']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_selected_items': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Product']"})
        },
        u'memecache.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_price': ('django.db.models.fields.IntegerField', [], {}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Transaction']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'memecache.shop': {
            'Meta': {'object_name': 'Shop'},
            'admin_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency_name': ('django.db.models.fields.CharField', [], {'default': "'MemeCache'", 'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segment': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['coplay.Segment']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'memecache.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['memecache.Account']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'number_of_items': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'total_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200'})
        }
    }

    complete_apps = ['memecache']
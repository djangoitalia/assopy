# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.www'
        db.delete_column('assopy_user', 'www')

        # Deleting field 'User.account_type'
        db.delete_column('assopy_user', 'account_type')

        # Deleting field 'User.city'
        db.delete_column('assopy_user', 'city')

        # Deleting field 'User.twitter'
        db.delete_column('assopy_user', 'twitter')

        # Deleting field 'User.skype'
        db.delete_column('assopy_user', 'skype')

        # Deleting field 'User.birthday'
        db.delete_column('assopy_user', 'birthday')

        # Deleting field 'User.tin_number'
        db.delete_column('assopy_user', 'tin_number')

        # Deleting field 'User.phone'
        db.delete_column('assopy_user', 'phone')

        # Deleting field 'User.state'
        db.delete_column('assopy_user', 'state')

        # Deleting field 'User.jabber'
        db.delete_column('assopy_user', 'jabber')

        # Deleting field 'User.photo'
        db.delete_column('assopy_user', 'photo')

        # Deleting field 'User.zip_code'
        db.delete_column('assopy_user', 'zip_code')

        # Deleting field 'Order.city'
        db.delete_column('assopy_order', 'city')

        # Deleting field 'Order.state'
        db.delete_column('assopy_order', 'state')

        # Deleting field 'Order.tin_number'
        db.delete_column('assopy_order', 'tin_number')

        # Deleting field 'Order.zip_code'
        db.delete_column('assopy_order', 'zip_code')


    def backwards(self, orm):
        # Adding field 'User.www'
        db.add_column('assopy_user', 'www',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'User.account_type'
        db.add_column('assopy_user', 'account_type',
                      self.gf('django.db.models.fields.CharField')(default='p', max_length=1),
                      keep_default=False)

        # Adding field 'User.city'
        db.add_column('assopy_user', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'User.twitter'
        db.add_column('assopy_user', 'twitter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'User.skype'
        db.add_column('assopy_user', 'skype',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'User.birthday'
        db.add_column('assopy_user', 'birthday',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.tin_number'
        db.add_column('assopy_user', 'tin_number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16, blank=True),
                      keep_default=False)

        # Adding field 'User.phone'
        db.add_column('assopy_user', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)

        # Adding field 'User.state'
        db.add_column('assopy_user', 'state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'User.jabber'
        db.add_column('assopy_user', 'jabber',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'User.photo'
        db.add_column('assopy_user', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.zip_code'
        db.add_column('assopy_user', 'zip_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)

        # Adding field 'Order.city'
        db.add_column('assopy_order', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'Order.state'
        db.add_column('assopy_order', 'state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'Order.tin_number'
        db.add_column('assopy_order', 'tin_number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16, blank=True),
                      keep_default=False)

        # Adding field 'Order.zip_code'
        db.add_column('assopy_order', 'zip_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5, blank=True),
                      keep_default=False)


    models = {
        'assopy.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numcode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'printable_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'vat_company': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vat_company_verify': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '1'}),
            'vat_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'assopy.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Conference']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'end_validity': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fares': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['conference.Fare']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_per_usage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'max_usage': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'start_validity': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.User']", 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'assopy.creditnote': {
            'Meta': {'object_name': 'CreditNote'},
            'assopy_id': ('django.db.models.fields.CharField', [], {'max_length': '22', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'emit_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'credit_notes'", 'to': "orm['assopy.Invoice']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'assopy.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'assopy_id': ('django.db.models.fields.CharField', [], {'max_length': '22', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True'}),
            'emit_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices'", 'to': "orm['assopy.Order']"}),
            'payment_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'vat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Vat']"})
        },
        'assopy.invoicelog': {
            'Meta': {'object_name': 'InvoiceLog'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Invoice']", 'null': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Order']", 'null': 'True'})
        },
        'assopy.order': {
            'Meta': {'object_name': 'Order'},
            '_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'assopy_id': ('django.db.models.fields.CharField', [], {'max_length': '22', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'billing_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'card_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Country']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'payment_url': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orders'", 'to': "orm['assopy.User']"}),
            'vat_number': ('django.db.models.fields.CharField', [], {'max_length': '22', 'blank': 'True'})
        },
        'assopy.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Order']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'ticket': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['conference.Ticket']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'vat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Vat']"})
        },
        'assopy.refund': {
            'Meta': {'object_name': 'Refund'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'credit_note': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['assopy.CreditNote']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'done': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Invoice']", 'null': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['assopy.OrderItem']", 'through': "orm['assopy.RefundOrderItem']", 'symmetrical': 'False'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'reject_reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '8'})
        },
        'assopy.refundorderitem': {
            'Meta': {'unique_together': "(('orderitem', 'refund'),)", 'object_name': 'RefundOrderItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orderitem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.OrderItem']"}),
            'refund': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Refund']"})
        },
        'assopy.token': {
            'Meta': {'object_name': 'Token'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ctype': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'payload': ('django.db.models.fields.TextField', [], {'blank': "''"}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'assopy.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'assopy_id': ('django.db.models.fields.CharField', [], {'max_length': '22', 'unique': 'True', 'null': 'True'}),
            'card_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Country']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '36', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'assopy_user'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'vat_number': ('django.db.models.fields.CharField', [], {'max_length': '22', 'blank': 'True'})
        },
        'assopy.useridentity': {
            'Meta': {'object_name': 'UserIdentity'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'display_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'phoneNumber': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'identities'", 'to': "orm['assopy.User']"})
        },
        'assopy.useroauthinfo': {
            'Meta': {'object_name': 'UserOAuthInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'oauth_infos'", 'to': "orm['assopy.User']"})
        },
        'assopy.vat': {
            'Meta': {'object_name': 'Vat'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'fares': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['conference.Fare']", 'null': 'True', 'through': "orm['assopy.VatFare']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_notice': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'})
        },
        'assopy.vatfare': {
            'Meta': {'unique_together': "(('fare', 'vat'),)", 'object_name': 'VatFare'},
            'fare': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Fare']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assopy.Vat']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'conference.conference': {
            'Meta': {'object_name': 'Conference'},
            'cfp_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cfp_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'conference_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'conference_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'voting_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'voting_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'conference.fare': {
            'Meta': {'unique_together': "(('conference', 'code'),)", 'object_name': 'Fare'},
            'blob': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'conference': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_validity': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '1'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'recipient_type': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '1'}),
            'start_validity': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'ticket_type': ('django.db.models.fields.CharField', [], {'default': "'conference'", 'max_length': '10', 'db_index': 'True'})
        },
        'conference.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'fare': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['conference.Fare']"}),
            'frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'ticket_type': ('django.db.models.fields.CharField', [], {'default': "'standard'", 'max_length': '8'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['assopy']
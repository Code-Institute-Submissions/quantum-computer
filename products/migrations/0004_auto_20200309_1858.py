# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-09 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200308_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='product_type',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-09 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200309_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('AMD_CPU', 'AMD CPU'), ('Intel_CPU', 'Intel CPU'), ('AMD_graphics_cards', 'AMD graphics cards'), ('Nvidia_graphics_cards', 'Nvidia graphics cards'), ('Motherboard', 'Motherboard'), ('Storage', 'Storage')], default='product type', max_length=30),
        ),
    ]

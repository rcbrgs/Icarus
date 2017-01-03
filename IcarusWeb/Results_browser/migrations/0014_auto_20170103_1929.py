# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Results_browser', '0013_auto_20170103_1928'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photophysiognomy',
            new_name='Phytophysiognomy',
        ),
        migrations.AlterField(
            model_name='sample',
            name='mosquitolab_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Results_browser.Mosquitolab'),
        ),
    ]

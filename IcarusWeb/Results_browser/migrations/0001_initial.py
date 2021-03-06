# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(max_length=255)),
                ('subgenus', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('subspecies', models.CharField(max_length=255)),
                ('family', models.CharField(max_length=255)),
                ('subfamily', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Results_browser.Classification')),
            ],
        ),
    ]

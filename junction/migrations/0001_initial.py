# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Junction',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('QaNum', models.IntegerField(default=0)),
                ('QbNum', models.IntegerField(default=0)),
                ('QcNum', models.IntegerField(default=0)),
                ('QdNum', models.IntegerField(default=0)),
                ('QabRat', models.FloatField(default=0.33)),
                ('QacRat', models.FloatField(default=0.33)),
                ('QadRat', models.FloatField(default=0.33)),
                ('QbaRat', models.FloatField(default=0.33)),
                ('QbcRat', models.FloatField(default=0.33)),
                ('QbdRat', models.FloatField(default=0.33)),
                ('QcaRat', models.FloatField(default=0.33)),
                ('QcbRat', models.FloatField(default=0.33)),
                ('QcdRat', models.FloatField(default=0.33)),
                ('QdaRat', models.FloatField(default=0.33)),
                ('QdbRat', models.FloatField(default=0.33)),
                ('QdcRat', models.FloatField(default=0.33)),
                ('visitNum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Qi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i', models.IntegerField()),
                ('macadd', models.CharField(max_length=20)),
                ('junctionNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='junction.Junction')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='junction',
            name='QabRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QacRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QadRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QbaRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QbcRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QbdRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QcaRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QcbRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QcdRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QdaRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QdbRat',
        ),
        migrations.RemoveField(
            model_name='junction',
            name='QdcRat',
        ),
        migrations.AddField(
            model_name='junction',
            name='Qab',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qac',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qad',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qba',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qbc',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qbd',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qca',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qcb',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qcd',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qda',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qdb',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='Qdc',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='junction',
            name='green',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='junction',
            name='isFirstPhase',
            field=models.BooleanField(default=True),
        ),
    ]

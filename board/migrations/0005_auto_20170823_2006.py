# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-23 23:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20170823_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='devolucao',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Devolucao'),
        ),
    ]
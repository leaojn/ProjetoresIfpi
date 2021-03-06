# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-25 02:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0004_projetor_manutencao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='Chave')),
                ('status', models.CharField(choices=[('O', 'Ocupado'), ('L', 'Livre')], default='L', max_length=1, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Laboratorio',
                'verbose_name_plural': 'Laboratorios',
            },
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitacoes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='laboratorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitacoes', to='board.Laboratorio'),
        ),
    ]

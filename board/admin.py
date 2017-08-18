# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment</i>'
    list_display = ('professor', 'cod_datashow','data_de_entrada')

    fieldsets = (
        (None, {
            'fields': (('professor', 'cod_datashow','data_de_saida'),)
        }),
    )

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">perm_identity</i>'
    # list_display = ('professor')

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
@admin.register(Projetor)
class ProjetorAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">video_label</i>'
    list_display = ('codigo','departamento','status')

    fieldsets = (
        (None, {
            'fields': ('codigo','departamento','observacao','manutencao')
        }),
    )

@admin.register(Departamento)
class DepatarmentAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">home</i>'
    list_display = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

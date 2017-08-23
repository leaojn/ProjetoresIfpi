# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment</i>'
    list_display = ('professor', 'data_show','data_de_entrada',)

    fieldsets = (
        (None, {
            'fields': (('professor', 'data_show',),)
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(SolicitacaoAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['data_show'].queryset = Projetor.objects.filter(manutencao=False, status=False)
        return form

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.data_show.status = True
            obj.data_show.save()
            devolucao = Devolucao()
            devolucao.save()
            obj.devolucao = devolucao
        obj.save()

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

@admin.register(Devolucao)
class DevolucaoAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment</i>'
    list_display = ('solicitacao', 'dt_horario_devolucao',)
    # readonly_fields = ['solicitacao_n']
    fieldsets = (
        (None, {
            'fields': (( 'status',),)
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.status == True:
            obj.dt_horario_devolucao = datetime.datetime.now()
            obj.save()
            solicitacao = Solicitacao.objects.get(devolucao=obj)
            solicitacao.data_show.status = False
            solicitacao.data_show.save()


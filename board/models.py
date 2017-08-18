# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Professor(models.Model):
    name =  models.CharField(max_length=100, blank=True,default='')

    def __str__(self):
        return self.name or _(' %s') % self.end

    class Meta:
        verbose_name = "Professor"


class Solicitacao(models.Model):
    professor = models.ForeignKey('Professor', related_name='solicitacoes')
    cod_datashow = models.CharField(max_length=100, blank=True,default='')
    data_de_entrada = models.DateTimeField('Data de entrada', auto_now_add=True)
    data_de_saida = models.DateTimeField('Data de entrada', auto_now_add=False)
    observacao = models.TextField('descricao', max_length=256, blank=True)


class Departamento(models.Model):
    name =  models.CharField(max_length=100, blank=True,default='')

    def __str__(self):
        return self.name or _(' %s') % self.end


class Projetor(models.Model):
    departamento = models.ForeignKey('Departamento',related_name='projetores')
    codigo = models.IntegerField(validators=[MaxValueValidator(999999)])
    status = models.BooleanField(default=True)
    manutencao = models.BooleanField(default=False)
    observacao = models.TextField('descricao', max_length=256, blank=True)





# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
# Create your models here.



STATUS = (
    ('D', 'Disponivel'),
    ('M', 'Manutenção'),
    ('U', 'Uso'),
    ('R', 'Reservado'),
)

class Professor(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.name or _(' %s') % self.end

    class Meta:
        verbose_name = 'Professor(a)'
        verbose_name_plural = 'Professores'


class Solicitacao(models.Model):
    professor = models.ForeignKey('Professor', related_name='solicitacoes')
    data_show = models.ForeignKey('Projetor', related_name='solicitacao')
    data_de_entrada = models.DateTimeField('Data de entrada', auto_now_add=True)
    observacao = models.TextField('descricao', max_length=256, blank=True)
    devolucao = models.OneToOneField('Devolucao', blank=True, null=True)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'

    @property
    def projetor_disponivel(self):
        return Projetor.objects.all().filter(manutencao=False)

    def __str__(self):
        return 'Professor(a):' + self.professor.name + '  ' + '[ Cod data show: ' + self.data_show.__str__() + ']'


class Departamento(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name or _(' %s') % self.end

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class Projetor(models.Model):
    departamento = models.ForeignKey('Departamento', related_name='projetores')
    codigo = models.IntegerField(validators=[MaxValueValidator(999999)])
    status= models.CharField(verbose_name='Status', max_length=1, choices=STATUS, default='D')
    observacao = models.TextField('descricao', max_length=256, blank=True)
    manutencao = models.BooleanField(blank=True, null=False, default=False)

    class Meta:
        verbose_name = 'Projetor'
        verbose_name_plural = 'Projetores'

    @property
    def projetor_manutencao(self):
        return Projetor.objects.filter(manutencao=True)

    @property
    def projetor_alugado(self):
        return Projetor.objects.filter(status=True)

    def __str__(self):
        return str(self.codigo)


class Devolucao(models.Model):
    dt_horario_devolucao = models.DateTimeField('Devolucao', auto_now_add=False, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Devoluçao'
        verbose_name_plural = 'Devoluçoes'



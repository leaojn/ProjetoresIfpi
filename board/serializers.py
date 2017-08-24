from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse
from .models import Solicitacao, Professor, Projetor
from django.contrib.auth import get_user_model
from datetime import date


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'name',)

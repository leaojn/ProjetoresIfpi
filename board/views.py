from rest_framework import viewsets, authentication, permissions
from .models import Professor
from .serializers import ProfessorSerializer
from django.contrib.auth import get_user_model

class ProfessorViewSet(viewsets.ModelViewSet):

    queryset = Professor.objects.order_by('name')
    serializer_class =ProfessorSerializer
    search_files = ('name')
    ordering_fields = ('name')
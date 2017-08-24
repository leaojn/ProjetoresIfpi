from rest_framework import viewsets, authentication, permissions
from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.order_by('name')
    serializer_class = ProfessorSerializer
    search_fields = ('name')
    ordering_fields = ('name')

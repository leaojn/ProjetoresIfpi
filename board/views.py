from rest_framework import viewsets, authentication, permissions
from .models import Professor
from .serializers import ProfessorSerializer
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.contrib.auth import get_user_model

class ProfessorViewSet(viewsets.ModelViewSet):

    queryset = Professor.objects.order_by('name')
    serializer_class =ProfessorSerializer
    search_fields = ('name')
    ordering_fields = ('name')

def pdf(request):
    template_name = 'pdf.html'
    pdf = canvas.Canvas("teste.pdf")
    pdf.drawString(100,100,"Hello Word")
    pdf.showPage()
    pdf.save()
    return "teste.pdf"
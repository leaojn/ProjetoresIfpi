from rest_framework import viewsets, authentication, permissions
from .models import Professor
from .serializers import ProfessorSerializer
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from board.models import Solicitacao
from board.utils import render_to_pdf  # created in step 4

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.order_by('name')
    serializer_class = ProfessorSerializer
    search_fields = ('name')
    ordering_fields = ('name')

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf_curriculo.html')
        context = {
            # "nome_id": request.user.user_curriculo.email,
            "obj": Solicitacao.objects.all(),
            "telefone" : '31313',
            # "email": request.user.email,
            # "rg": request.user.user_curriculo.rg,
            # "endereco": request.user.user_curriculo.endereco,
            # "cpf": request.user.user_curriculo.cpf,
            # "objetivo": request.user.user_curriculo.objetivo,
            # "data_nascimento": request.user.user_curriculo.data_nascimento,
            # "serie": request.user.user_curriculo.serie,
            # "formacao_academica": request.user.user_curriculo.formacao_academica,
            # "cursos_extras": request.user.user_curriculo.cursos_extras,
            # "experiencia_profissional": request.user.user_curriculo.experiencia_profissional,
            # "participacao_eventos": request.user.user_curriculo.participacao_eventos,
        }
        html = template.render(context)

        pdf = render_to_pdf('pdf_curriculo.html', context)
        if pdf:
            reponse = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" % (filename)

            download = request.GET.get("download")
            if download:
                content = "attachement; filename='%s'" % (filename)
            reponse['Content-Disposition'] = content
            return reponse
        return  HttpResponse("Not Found")

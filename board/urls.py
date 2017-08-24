from rest_framework.routers import DefaultRouter

from .views import GeneratePdf
# from .views import vi
from django.conf.urls import url


router = DefaultRouter()

# router.register(r'professores', views.ProfessorViewSet)
urlpatterns = [

    url('^pdf/$', GeneratePdf.as_view(), name='gerar-pdf'),


]
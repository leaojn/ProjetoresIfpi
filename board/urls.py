from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'professores', views.ProfessorViewSet)
from django.conf.urls import url,include
from .views import pdf

urlpatterns = [
    url('^pdf/$', views.pdf, name='meus_eventos'),

]
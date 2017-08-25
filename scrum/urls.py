"""scrum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.contrib.auth import views as auth_views
from board.urls import router
from board.views import GeneratePdf
from django.contrib.contenttypes import views as contenttype_views

template = "templates/admin/login.html"
urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^', admin.site.urls, name='admin'),
    # url(r'^api/', include(router.urls)),
    url(r'^login/$', auth_views.login, {'template_name': template}, name='login'),
    # url('^', include('board.urls', namespace="board")),

]
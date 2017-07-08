# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, authentication, permissions
from .forms import TaskFilter, SprintFilter
from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class SprintViewSet(viewsets.ModelViewSet):

    queryset = Sprint.objects.order_by('end')
    serializer_class =SprintSerializer
    search_files = ('name')
    ordering_fields = ('name','end')

class DefaultMixin(object):

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class TaskViewSet(DefaultMixin, viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    search_fields = ('name', 'description')
    ordering_fields = ('name','order','started','due','completed')

class UserViewSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD)